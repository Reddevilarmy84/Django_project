import os
import json
import math

path_to_json_DM = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Dungeon_master.json')

class Mob:
    pass

class Hero:
    hero = {
        'hp':200,
        'hp_max':200,
        'mp': 200,
        'mp_max': 200,
        'exp': 0,
        'exp_to_lvl': 70,
        'lvl': 1,
        'pwr': 10,
    }

    spec1 = 'огненный шар'
    spec1_mp = 20
    spec1_pwr = 0
    spec2 = 'огненный шторм'
    spec2_mp = 30
    spec2_pwr = 0
    spec3 = 'плазменный взрыв'
    spec3_mp = 50
    spec3_pwr = 0

    def up_lvl(self, lvl):
        self.hero['lvl'] += lvl
        self.hero['hp_max'] += lvl*40
        self.hero['hp'] = self.hero['hp_max']
        self.hero['pwr'] += lvl*5
        self.hero['mp'] = self.hero['mp_max']
        self.hero['exp_to_lvl'] += 110
        self.spec1_pwr = math.floor(self.hero['lvl']/2) * 9
        self.spec1_mp += (lvl * 10)
        self.spec2_mp += lvl * 14
        self.spec2_pwr = math.floor(self.hero['lvl']/5) * 38
        self.spec3_mp += lvl * 19
        self.spec3_pwr = math.floor(self.hero['lvl']/10) * 147

    def hp_bar(self):
        return int( self.hero['hp'] / self.hero['hp_max'] * 300 )
    def mp_bar(self):
        return int( self.hero['mp'] / self.hero['mp_max'] * 300 )

class Location:
    location = {'img': 'main/img/locations/loc_0.jpg'}
    length = 10
    path_traveled = 0


class Colors:
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    light_blue = '\033[36m'
    grey = '\033[37m'

    black_back = '\033[40m'
    red_back = '\033[41m'
    green_back = '\033[42m'
    yellow_back = '\033[43m'
    blue_back = '\033[44m'
    purple_back = '\033[45m'
    light_blue_back = '\033[46m'
    grey_back = '\033[47m'

    reset = '\033[0m'  #сброс
    bolt = '\033[1m'  #жирный
    light = '\033[2m'  #Блёклый
    curs = '\033[3m'  #Курсив
    line = '\033[4m'  #Подчёркнутый
    blink = '\033[5m'  # Редкое мигание
    blink_fast = '\033[6m'  # Частое мигание
    inv = '\033[7m'  # Смена цвета фона с цветом текста

def dict_to_json(dict_list, filename):
    try:
        json_str = json.dumps(dict_list, ensure_ascii=False)
        with open(filename, "w+", encoding="utf-8") as file:
            file.write(json_str)
        return json_str
    except (TypeError, ValueError, IOError) as e:
        print(f"Ошибка при преобразовании списка словарей в JSON или записи в файл: {e}")
        return None


def json_to_dict(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            json_str = file.read()
            dict_list = json.loads(json_str)
        return dict_list
    except (TypeError, ValueError, IOError) as e:
        print(f"Ошибка при чтении JSON из файла или преобразовании в список словарей: {e}\n"
              f"Фаёл films.json пересоздан")
        with open(filename, "w+", encoding="utf-8") as file:
            json_str = '[]'
            file.write(json_str)
        with open(filename, "r", encoding="utf-8") as file:
            json_str = file.read()
            dict_list = json.loads(json_str)
        return dict_list