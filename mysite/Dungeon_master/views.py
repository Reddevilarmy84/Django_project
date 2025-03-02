from django.shortcuts import render
from .Dungeon_master import dict_to_json, json_to_dict, path_to_json_DM, Colors, Hero, Mob, Location

player = Hero()
mob = Mob()
location = Location()

def Dungeon_master(request, action: str = None):
    print(location.location['img'])
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

    if not player.hero and phase != "choose_hero":
        for i in json:
            if i["id"] == "config":
                i["phase"] = "title"
    print(f"действие: {action}")
    #отслеживание фаз
    if phase == "title":
        if action == "start_game":
            for i in json:
                if i["id"] == "config":
                    i["phase"] = "choose_hero"
    # отслеживание фазы выбор героя
    if phase == "choose_hero":
        if action == "mage" or action == "warior" or action == "chief":
            player.type = action
            player.hero['img'] = f"main/img/{action}" + ".jpg"
            for i in json:
                if i["id"] == "config":
                    i["phase"] = "choose_location"
    # отслеживание фазы выбор локации
    if phase == "choose_location":
        if action == "cave_1":
            location.location['img'] = 'main/img/locations/loc_1.jpg'
            location.length = 10
            location.path_traveled = 0
            for i in json:
                if i["id"] == "config":
                    i["phase"] = "exploration"
    # отслеживание фазы локации
    if phase == "exploration":
        print(f"Пройдено: {location.path_traveled}")
        if action == "do_step":
            if location.path_traveled == location.length-1:
                location.path_traveled += 1
                for i in json:
                    if i["id"] == "config":
                        i["phase"] = "exploration_completed"
                        print("Локация пройдена")
            else:
                location.path_traveled += 1
    # отслеживание фазы локация пройдена
    if phase == "exploration_completed":
        if action == "complete":
            for i in json:
                if i["id"] == "config":
                    i["phase"] = "choose_location"
            location.path_traveled = 0
            player.hero['exp'] += 100
            if player.hero['exp'] >= player.hero['exp_to_lvl']:
                player.up_lvl(1)


    print(json)
    dict_to_json(json, path_to_json_DM)
    context = {
        'title': 'MadJunior: повелитель пещер',
        'header': 'повелитель пещер',
        'json': json,
        'player': player,
        'mob': mob,
        'location': location,
    }
    return render(request, 'Dungeon_master/main.html', context)