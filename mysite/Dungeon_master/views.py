from django.shortcuts import render
from .Dungeon_master import dict_to_json, json_to_dict, path_to_json_DM, Colors, Hero, Mob, Location, Game
import re
import random

hero = Hero()
mob = Mob()
location = Location()
game = Game()

def Dungeon_master(request, action: str = None):
    json = json_to_dict(path_to_json_DM)
    action = request.GET.get('action', action)
    if not game.game:
        for i in json:
            if i["id"] == "config":
                i["phase"] = "title"
                game.game = True
                print(f"Установлен title")

    if action == "exit":
        for i in json:
            if i["id"] == "config":
                i["phase"] = "title"
        hero.stats.clear()
        mob.stats.clear()
        hero.content.clear()
        mob.content.clear()
        hero.current_attack.clear()
        mob.current_attack.clear()
        hero.fury = False

    try:
        phase = [i['phase'] for i in json if i["id"] == "config"][0]
    except:
        print(f"фаза не найдена")
        phase = None

    if action == 'potion_heal':
        print(hero.stats['hp'], hero.stats['hp_max'])
        if hero.stats['hp'] < hero.stats['hp_max']:
            hero.potions['heal'] -= 1
            hero.stats['hp'] += int(hero.stats['hp_max']/2)
            hero.stats['hp'] = hero.stats['hp'] if hero.stats['hp'] <= hero.stats['hp_max'] else hero.stats['hp_max']

    if action == 'potion_mana':
        print(hero.stats['mp'], hero.stats['mp_max'])
        if hero.stats['mp'] < hero.stats['mp_max']:
            hero.potions['mana'] -= 1
            hero.stats['mp'] += int(hero.stats['mp_max'] / 2)
            hero.stats['mp'] = hero.stats['mp'] if hero.stats['mp'] <= hero.stats['mp_max'] else hero.stats['mp_max']

    if action == 'potion_fury':
        hero.potions['fury'] = hero.potions['fury'] - 1 if not hero.fury else hero.potions['fury']
        hero.fury = 10 if not hero.fury and hero.potions['fury'] else hero.fury

    hero.fury = hero.fury - 1 if hero.fury and phase == "hero_attack" and re.match('attack', action) else hero.fury

    #отслеживание фазы title
    if phase == "title":
        if action == "start_game":
            for i in json:
                if i["id"] == "config":
                    i["phase"] = "choose_hero"

    # отслеживание фазы выбор героя
    if phase == "choose_hero":
        if re.match('hero', action):
            hero.choose_hero(int(list(action)[-1]))
            hero.potions['heal'], hero.potions['mana'], hero.potions['fury'] = 3, 3, 3
            for i in json:
                if i["id"] == "config":
                    i["phase"] = "choose_location"

    # отслеживание фазы выбор локации
    if phase == "choose_location":
        if  re.match("cave", action):
            location.content = dict(location.content_list[int(list(action)[-1])].items())
            location.stats = dict(location.stats_list[int(list(action)[-1])].items())
            for i in json:
                if i["id"] == "config":
                    i["phase"] = "exploration"

    # отслеживание фазы локации
    if phase == "exploration":
        if action == "do_step":
            if location.stats['completed'] == location.stats['length']-1:
                location.stats['completed'] += 1
                for i in json:
                    if i["id"] == "config":
                        i["phase"] = "exploration_completed"
            else:
                chance = random.randrange(100)
                if location.stats['chance_mob'] >= chance:
                    mob.set_mob()
                    mob.set_lvl_mob(random.randint(location.stats['dificult'] - 2 + hero.stats['lvl'], location.stats['dificult'] + 2 + hero.stats['lvl']))
                    mob.attack(random.randrange(4))
                    mob.current_attack['pwr'] = None
                    for i in json:
                        if i["id"] == "config":
                            i["phase"] = "meet_mob"
                location.stats['completed'] += 1

    # отслеживание фазы встреча моба
    if phase == "meet_mob":
        if action == "enter_the_battle":
            for i in json:
                if i["id"] == "config":
                    i["phase"] = random.choice(["hero_attack", "mob_attack"])

    # отслеживание атака моба
    if phase == "mob_attack":
        hero.current_attack['pwr'] = None
        mob.attack(random.randrange(4))
        hero.stats['hp_before'] = int(hero.stats['hp'] / hero.stats['hp_max'] * 300) #получаем целое число
        hero.stats['hp'] -= mob.current_attack['pwr']
        for i in json:
            if i["id"] == "config":
                i["phase"] = "hero_attack"
        if hero.stats['hp'] <= 0:
            hero.stats['hp'] = 0
            hero.potions['heal'] = 0
            hero.potions['mana'] = 0
            hero.potions['fury'] = 0
            for i in json:
                if i["id"] == "config":
                    i["phase"] = "battle_loose"
                    location.stats['completed'] = 0

    # отслеживание атака героя
    if phase == "hero_attack":
        mob.current_attack['pwr'] = None
        hero.stats['hp_before'] = int(hero.stats['hp'] / hero.stats['hp_max'] * 300) #получаем целое число
        if re.match('attack', action):
            hero.attack(int(list(action)[-1]))
            hero.current_attack['pwr'] = int(hero.current_attack['pwr']*1.3) if hero.fury else hero.current_attack['pwr']
            mob.stats['hp'] -= hero.current_attack['pwr']
            for i in json:
                if i["id"] == "config":
                    i["phase"] = "mob_attack"
            if mob.stats['hp'] <= 0:
                mob.stats['hp'] = 0
                hero.stats['exp'] += mob.stats['exp']
                while hero.stats['exp'] >= hero.stats['exp_to_lvl']:
                    hero.stats['exp'] -= hero.stats['exp_to_lvl']
                    hero.up_lvl(1)
                hero.stats['hp_before'] = int(hero.stats['hp'] / hero.stats['hp_max'] * 300)  # получаем целое число
                for i in json:
                    if i["id"] == "config":
                        i["phase"] = "battle_win"

    # отслеживание герой победил
    if phase == "battle_win":
        if action == "do_step":
            for i in json:
                if i["id"] == "config":
                    i["phase"] = "exploration"
                    hero.current_attack.clear()
                    mob.current_attack.clear()


    # отслеживание фазы локация пройдена
    if phase == "exploration_completed":
        if action == "complete":
            for i in json:
                if i["id"] == "config":
                    i["phase"] = "choose_location"
            location.stats['completed'] = 0
            hero.fury = False



    print(f'Фаза: {phase} Действие: {action}')
    dict_to_json(json, path_to_json_DM)
    context = {
        'title': 'MadJunior: Повелитель Пещер',
        'header': 'Повелитель Пещер',
        'json': json,
        'hero': hero,
        'mob': mob,
        'location': location,
    }
    return render(request, 'Dungeon_master/battle.html', context)