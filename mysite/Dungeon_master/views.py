from django.shortcuts import render
from .Dungeon_master import dict_to_json, json_to_dict, path_to_json_DM, Colors, Hero, Mob, Location
import re

hero = Hero()
mob = Mob()
location = Location()

def Dungeon_master(request, action: str = None):
    print(location.content['img'])
    json = json_to_dict(path_to_json_DM)
    action = request.GET.get('action', action)

    if action == "exit":
        for i in json:
            if i["id"] == "config":
                i["phase"] = "title"
    try:
        phase = [i['phase'] for i in json if i["id"] == "config"][0]
        print(f"фаза: {phase}")
    except:
        print(f"фаза не найдена")
        phase = None


    print(f"действие: {action}")
    #отслеживание фаз
    if phase == "title":
        if action == "start_game":
            for i in json:
                if i["id"] == "config":
                    i["phase"] = "choose_hero"
            if hero.stats:
                for i in json:
                    if i["id"] == "config":
                        i["phase"] = "choose_location"
    # отслеживание фазы выбор героя
    if phase == "choose_hero":
        if re.match('hero', action):
            hero.content = hero.content_list[int(list(action)[-1])]
            hero.stats = hero.stats_list[int(list(action)[-1])]
            print(f'статы:{hero.stats}\nконтент:{hero.content}')
            for i in json:
                if i["id"] == "config":
                    i["phase"] = "choose_location"
    # отслеживание фазы выбор локации
    if phase == "choose_location":
        if  re.match("cave", action):
            location.content = location.content_list[int(list(action)[-1])]
            location.stats = location.stats_list[int(list(action)[-1])]
            print(location.content)
            print(location.stats)
            for i in json:
                if i["id"] == "config":
                    i["phase"] = "exploration"
    # отслеживание фазы локации
    if phase == "exploration":
        print(f"Пройдено: {location.stats['completed']}")
        if action == "do_step":
            if location.stats['completed'] == location.stats['length']-1:
                location.stats['completed'] += 1
                for i in json:
                    if i["id"] == "config":
                        i["phase"] = "exploration_completed"
                        print("Локация пройдена")
            else:
                location.stats['completed'] += 1
    # отслеживание фазы локация пройдена
    if phase == "exploration_completed":
        if action == "complete":
            for i in json:
                if i["id"] == "config":
                    i["phase"] = "choose_location"
            location.stats['completed'] = 0
            hero.stats['exp'] += 100
            if hero.stats['exp'] >= hero.stats['exp_to_lvl']:
                hero.stats['exp'] -= hero.stats['exp_to_lvl']
                hero.up_lvl(1)



    dict_to_json(json, path_to_json_DM)
    context = {
        'title': 'MadJunior: Повелитель Пещер',
        'header': 'Повелитель Пещер',
        'json': json,
        'hero': hero,
        'mob': mob,
        'location': location,
    }
    return render(request, 'Dungeon_master/main.html', context)