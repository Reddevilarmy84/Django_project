from django.shortcuts import render
from .Dungeon_master import dict_to_json, json_to_dict, path_to_json_DM, Colors, Mage, Mob
player = Mage()
mob = Mob()


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


    print(json)
    dict_to_json(json, path_to_json_DM)
    context = {
        'title': 'MadJunior: повелитель пещер',
        'header': 'повелитель пещер',
        'json': json,
        'player': player,
        'mob': mob,
    }
    return render(request, 'Dungeon_master/main.html', context)