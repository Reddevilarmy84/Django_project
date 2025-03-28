from .Dungeon_master import dict_to_json, json_to_dict, path_to_json_DM, Hero, Mob, Location, Game, Loot
from django.shortcuts import render
import random
import re

mob = None
hero = None
game = None
location = None
loot = None

def Dungeon_master(request, action: str = None):
    global hero, mob, game, location, loot
    loot = Loot() if not loot else loot
    hero = Hero() if not hero else hero
    mob = Mob() if not mob else mob
    game = Game() if not game else game
    location = Location() if not location else location
    action = request.GET.get('action', action)
    phase = game.phase
    game.action = action
    if action == "exit":
        loot = Loot() if not loot else loot
        hero = Hero() if not hero else hero
        mob = Mob() if not mob else mob
        game = Game() if not game else game
        location = Location() if not location else location
        game.phase = 'title'
        phase = 'title'
        hero.stats.clear()
        mob.stats.clear()
        hero.content.clear()
        mob.content.clear()
        hero.current_attack.clear()
        mob.current_attack.clear()
        for k in hero.condition.keys():
            hero.condition[k] = False
        print(hero.condition.values())
    if action == 'potion_heal' and hero.stats['hp'] < hero.stats['hp_max'] and not hero.condition['heal']:
        hero.potions['heal'] = hero.potions['heal'] - 1 if not hero.condition['heal'] else hero.potions['heal']
        hero.condition['heal'] = 5 if not hero.condition['heal'] and hero.potions['heal'] else hero.condition['heal']
        hero.stats['hp'] += int(hero.stats['hp_max']/2)
        print(int(hero.stats['hp_max']/2))
        hero.stats['hp'] = hero.stats['hp'] if hero.stats['hp'] <= hero.stats['hp_max'] else hero.stats['hp_max']
    if action == 'potion_mana' and hero.stats['mp'] < hero.stats['mp_max']:
        hero.potions['mana'] = hero.potions['mana'] - 1 if not hero.condition['mana'] else hero.potions['mana']
        hero.condition['mana'] = 5 if not hero.condition['mana'] else hero.condition['mana']
        hero.stats['mp'] += int(hero.stats['mp_max'] / 2)
        hero.stats['mp'] = hero.stats['mp'] if hero.stats['mp'] <= hero.stats['mp_max'] else hero.stats['mp_max']
    if action == 'potion_fury':
        hero.potions['fury'] = hero.potions['fury'] - 1 if not hero.condition['fury'] else hero.potions['fury']
        hero.condition['fury'] = 10 if not hero.condition['fury'] else hero.condition['fury']
    if action == 'potion_shield':
        hero.potions['shield'] = hero.potions['shield'] - 1 if not hero.condition['shield'] else hero.potions['shield']
        hero.condition['shield'] = 10 if not hero.condition['shield'] else hero.condition['shield']
    if action == 'potion_spikes':
        hero.potions['spikes'] = hero.potions['spikes'] - 1 if not hero.condition['spikes'] else hero.potions['spikes']
        hero.condition['spikes'] = 10 if not hero.condition['spikes'] else hero.condition['spikes']

        print('нет атрибутов')
    #отслеживание фазы title
    game.phase = 'choose_hero' if game.phase == "title" and action == "start_game" else game.phase
    # отслеживание фазы выбор героя
    if phase == "choose_hero" and re.match('hero', action):
        hero.choose_hero(int(list(action)[-1]))

        game.phase = "choose_location"
    # отслеживание фазы выбор локации
    if phase == "choose_location" and re.match("cave", action):
        location.content = dict(location.content_list[int(list(action)[-1])].items())
        location.stats = dict(location.stats_list[int(list(action)[-1])].items())
        game.phase = "exploration"
    # отслеживание фазы локации
    if phase == "exploration" and action == "do_step":
        if location.stats['completed'] == location.stats['length']-1:
            location.stats['completed'] += 1
            game.phase = "exploration_completed"
        else:
            chance = random.randrange(100)
            if location.stats['chance_mob'] >= chance:
                mob.set_mob()
                mob.set_lvl_mob(random.randint(location.stats['dificult'] - 2 + hero.stats['lvl'], location.stats['dificult'] + 2 + hero.stats['lvl']))
                mob.attack(random.randrange(4))
                mob.current_attack['pwr'] = None
                game.phase = "meet_mob"
            location.stats['completed'] += 1
    # отслеживание фазы встреча моба
    game.phase = random.choice(["hero_attack", "mob_attack"]) if game.phase == "meet_mob" and action == "enter_the_battle" else game.phase
    # отслеживание атака моба
    if phase == "mob_attack":
        hero.current_attack['pwr'] = None
        mob.attack(random.randrange(4))
        hero.stats['hp_before'] = int(hero.stats['hp'] / hero.stats['hp_max'] * 300)
        # если активно состояние героя щит то хп героя уменьшается на 50% меньше. результат деления - это целое число
        hero.stats['hp'] = hero.stats['hp'] - int(mob.current_attack['pwr']/2) if hero.condition['shield'] else hero.stats['hp'] - mob.current_attack['pwr']
        # если активно состояние героя шипы то хп моба уменьшается на 50% от его атаки. результат деления - это целое число
        mob.stats['hp'] = mob.stats['hp'] - int(mob.current_attack['pwr']/2) if hero.condition['spikes'] else mob.stats['hp']
        game.phase = "hero_attack"
        if hero.stats['hp'] <= 0:
            hero.stats['hp'] = 0
            for v in hero.potions.values():
                v = False
            for v in hero.condition.values():
                v = False
            game.phase = "battle_loose"
            location.stats['completed'] = 0

    # отслеживание атака героя
    if phase == "hero_attack":
        mob.current_attack['pwr'] = None
        hero.stats['hp_before'] = int(hero.stats['hp'] / hero.stats['hp_max'] * 300) #получаем целое число
        if re.match('hero_attack', action):
            hero.attack(int(list(action)[-1]))
            hero.current_attack['pwr'] = int(hero.current_attack['pwr']*1.3) if hero.condition['fury'] else hero.current_attack['pwr']
            mob.stats['hp'] -= hero.current_attack['pwr']
            game.phase = "mob_attack"
            if mob.stats['hp'] <= 0:
                mob.stats['hp'] = 0
                hero.stats['exp'] += mob.stats['exp']
                while hero.stats['exp'] >= hero.stats['exp_to_lvl']:
                    hero.stats['exp'] -= hero.stats['exp_to_lvl']
                    hero.up_lvl(1)
                hero.stats['hp_before'] = int(hero.stats['hp'] / hero.stats['hp_max'] * 300)  # получаем целое число
                game.phase = "battle_win"
                loot.bounty(10)
                current_keys = []
                current_values = []
                for item in loot.bount:
                    current_keys.append(item['name'])
                for item in loot.bount:
                    current_values.append(item['quantity'])
                current_potions = dict(zip(current_keys, current_values))
                for i in current_potions.keys():
                    hero.potions[i] += current_potions[i]
                loot.bount.append({'name': 'exp', 'img': 'main/img/items/exp.jpg', 'quantity': mob.stats['exp']})
                print(loot.bount)
    # отслеживание герой победил
    if phase == "battle_win" and action == "do_step":
        game.phase = "exploration"
        hero.current_attack.clear()
        mob.current_attack.clear()

    # отслеживание фазы локация пройдена
    if phase == "exploration_completed" and action == "complete":
        game.phase = "choose_location"
        location.stats['completed'] = 0
        hero.condition = dict((k, False) for k, v in hero.condition.items())
    # обработка бонуса за состояния и алгоритмы убывания состояния
    if phase == 'hero_attack' or phase =='mob_attack':
        # восстанавливаем 20% хп каждый ход пока действует состояние хил
        hero.stats['hp'] = hero.stats['hp'] + int(hero.stats['hp_max'] / 5) if hero.condition['heal'] and re.search(
            'attack', action) else hero.stats['hp']
        # восстановленное хп не должно превышать максимальное хп
        hero.stats['hp'] = hero.stats['hp_max'] if hero.stats['hp'] > hero.stats['hp_max'] else hero.stats['hp']
        # восстанавливаем 20% мп каждый ход пока действует состояние мана
        hero.stats['mp'] = hero.stats['mp'] + int(hero.stats['mp_max'] / 5) if hero.condition['mana'] and re.search(
            'attack', action) else hero.stats['mp']
        # восстановленное мп не должно превышать максимальное мп
        hero.stats['mp'] = hero.stats['mp_max'] if hero.stats['mp'] > hero.stats['mp_max'] else hero.stats['mp']
        hero.condition['heal'] = hero.condition['heal'] - 1 if hero.condition['heal'] and re.search('attack', action) else hero.condition['heal']
        hero.condition['mana'] = hero.condition['mana'] - 1 if hero.condition['mana'] and re.search('attack', action) else hero.condition['mana']
        hero.condition['fury'] = hero.condition['fury'] - 1 if hero.condition['fury'] and re.search('hero_attack', action) else hero.condition['fury']
        hero.condition['shield'] = hero.condition['shield'] - 1 if hero.condition['shield'] and re.search(
            'mob_attack', action) else hero.condition['shield']
        hero.condition['spikes'] = hero.condition['spikes'] - 1 if hero.condition['spikes'] and re.search(
            'mob_attack', action) else hero.condition['spikes']
    context = {
        'game': game,
        'hero': hero,
        'mob': mob,
        'location': location,
        'loot': loot,
    }
    return render(request, 'Dungeon_master/battle.html', context)