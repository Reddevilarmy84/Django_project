from .Dungeon_master import dict_to_json, json_to_dict, path_to_json_DM, Hero, Mob, Location, Game
from django.shortcuts import render
import random
import re
mob = Mob()
hero = Hero()
game = Game()
location = Location()


def Dungeon_master(request, action: str = None):
    action = request.GET.get('action', action)
    phase = game.phase
    if action == "exit":
        game.phase = 'title'
        phase = 'title'
        hero.stats.clear()
        mob.stats.clear()
        hero.content.clear()
        mob.content.clear()
        hero.current_attack.clear()
        mob.current_attack.clear()
        hero.fury = False
    if action == 'potion_heal' and hero.stats['hp'] < hero.stats['hp_max']:
        hero.potions['heal'] -= 1
        hero.stats['hp'] += int(hero.stats['hp_max']/2)
        hero.stats['hp'] = hero.stats['hp'] if hero.stats['hp'] <= hero.stats['hp_max'] else hero.stats['hp_max']
    if action == 'potion_mana' and hero.stats['mp'] < hero.stats['mp_max']:
        hero.potions['mana'] -= 1
        hero.stats['mp'] += int(hero.stats['mp_max'] / 2)
        hero.stats['mp'] = hero.stats['mp'] if hero.stats['mp'] <= hero.stats['mp_max'] else hero.stats['mp_max']
    if action == 'potion_fury':
        hero.potions['fury'] = hero.potions['fury'] - 1 if not hero.fury else hero.potions['fury']
        hero.fury = 10 if not hero.fury and hero.potions['fury'] else hero.fury
    hero.fury = hero.fury - 1 if hero.fury and game.phase == "hero_attack" and re.match('attack', action) else hero.fury
    #отслеживание фазы title
    game.phase = 'choose_hero' if game.phase == "title" and action == "start_game" else game.phase
    # отслеживание фазы выбор героя
    if phase == "choose_hero" and re.match('hero', action):
        hero.choose_hero(int(list(action)[-1]))
        hero.potions['heal'], hero.potions['mana'], hero.potions['fury'] = 3, 3, 3
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
        hero.stats['hp_before'] = int(hero.stats['hp'] / hero.stats['hp_max'] * 300) #получаем целое число
        hero.stats['hp'] -= mob.current_attack['pwr']
        game.phase = "hero_attack"
        if hero.stats['hp'] <= 0:
            hero.stats['hp'] = 0
            hero.potions['heal'] = 0
            hero.potions['mana'] = 0
            hero.potions['fury'] = 0
            game.phase = "battle_loose"
            location.stats['completed'] = 0

    # отслеживание атака героя
    if phase == "hero_attack":
        mob.current_attack['pwr'] = None
        hero.stats['hp_before'] = int(hero.stats['hp'] / hero.stats['hp_max'] * 300) #получаем целое число
        if re.match('attack', action):
            hero.attack(int(list(action)[-1]))
            hero.current_attack['pwr'] = int(hero.current_attack['pwr']*1.3) if hero.fury else hero.current_attack['pwr']
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
    # отслеживание герой победил
    if phase == "battle_win" and action == "do_step":
        game.phase = "exploration"
        hero.current_attack.clear()
        mob.current_attack.clear()
    # отслеживание фазы локация пройдена
    if phase == "exploration_completed" and action == "complete":
        game.phase = "choose_location"
        location.stats['completed'] = 0
        hero.fury = False
    context = {
        'title': 'MadJunior: Повелитель Пещер',
        'header': 'Повелитель Пещер',
        'game': game,
        'hero': hero,
        'mob': mob,
        'location': location,
    }
    return render(request, 'Dungeon_master/battle.html', context)