from django.shortcuts import render
from .Dungeon_master import dict_to_json, json_to_dict, path_to_json_DM, Colors, Hero, Mob, Location

player = Hero()
mob = Mob()
loc = Location()

def Dungeon_master(request, action: str = None):
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
    # отслеживание фазы выбор героя
    if phase == "choose_hero":
        if action == "mage" or action == "warior" or action == "chief":
            player.type = action
            player.img = f"main/img/{action}" + ".jpg"
            for i in json:
                if i["id"] == "config":
                    i["phase"] = "choose_location"
    # отслеживание фазы выбор локации
    if phase == "choose_location":
        if action == "cave_1":
            loc.length = 10
            loc.path_traveled = 0
            for i in json:
                if i["id"] == "config":
                    i["phase"] = "exploration"
    # отслеживание фазы локации
    if phase == "exploration":
        print(f"Пройдено: {loc.path_traveled}")
        if action == "do_step":
            if loc.path_traveled == loc.length-1:
                loc.path_traveled += 1
                for i in json:
                    if i["id"] == "config":
                        i["phase"] = "exploration_completed"
                        print("Локация пройдена")
            else:
                loc.path_traveled += 1
    # отслеживание фазы локация пройдена
    if phase == "exploration_completed":
        if action == "complete":
            for i in json:
                if i["id"] == "config":
                    i["phase"] = "choose_location"
            loc.path_traveled = 0
            player.exp += 100
            if player.exp >= player.exp_to_lvl:
                player.up_lvl(1)


    print(json)
    dict_to_json(json, path_to_json_DM)
    context = {
        'title': 'MadJunior: повелитель пещер',
        'header': 'повелитель пещер',
        'json': json,
        'player': player,
        'mob': mob,
        'loc': loc,
    }
    return render(request, 'Dungeon_master/main.html', context)