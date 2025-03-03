import os
import json
import math

path_to_json_DM = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Dungeon_master.json')

class Mob:
    pass

class Hero:
    current_attack = {}
    content = {}
    stats = {}
    stats_list = [
        {
            'id': 'hero_0',
            'lvl': 1,
            'attack_pwr': 10,
            'hp':50,
            'hp_max':50,
            'hp_before': 50,
            'mp': 100,
            'mp_max': 100,
            'mp_before': 100,
            'exp': 0,
            'exp_to_lvl': 100,
            'exp_before': 100,
            'spec1_pwr': 20,
            'spec2_pwr': 30,
            'spec3_pwr': 40,
            'spec1_mp': 20,
            'spec2_mp': 30,
            'spec3_mp': 40,
        },
        {
            'id': 'hero_1',
            'lvl': 1,
            'attack_pwr': 10,
            'hp': 50,
            'hp_max': 50,
            'hp_before': 50,
            'mp': 100,
            'mp_max': 100,
            'mp_before': 100,
            'exp': 0,
            'exp_to_lvl': 100,
            'exp_before': 100,
            'spec1_pwr': 20,
            'spec2_pwr': 30,
            'spec3_pwr': 40,
            'spec1_mp': 20,
            'spec2_mp': 30,
            'spec3_mp': 40,
        },
        {
            'id': 'hero_2',
            'lvl': 1,
            'attack_pwr': 10,
            'hp': 50,
            'hp_max': 50,
            'hp_before': 50,
            'mp': 100,
            'mp_max': 100,
            'mp_before': 100,
            'exp': 0,
            'exp_to_lvl': 100,
            'exp_before': 100,
            'spec1_pwr': 20,
            'spec2_pwr': 30,
            'spec3_pwr': 40,
            'spec1_mp': 20,
            'spec2_mp': 30,
            'spec3_mp': 40,
        },
]
    content_list = [
        {
            'class': 'маг',
            'img': 'main/img/hero/hero_0.jpg',
            'spec1': 'огненный шар',
            'spec2': 'ледяной шторм',
            'spec3': 'солнечная вспышка',
            'spec1_img': '',
            'spec2_img': '',
            'spec3_img': '',
        },
        {
            'class': 'воин',
            'img': 'main/img/hero/hero_1.jpg',
            'spec1': 'рассечение',
            'spec2': 'выпад силы',
            'spec3': 'снизхождение',
            'spec1_img': '',
            'spec2_img': '',
            'spec3_img': '',
        },
        {
            'class': 'вор',
            'img': 'main/img/hero/hero_2.jpg',
            'spec1': 'удар в спину',
            'spec2': 'выстрел из арбалета',
            'spec3': 'атака тени',
            'spec1_img': '',
            'spec2_img': '',
            'spec3_img': '',
        },
    ]

    def up_lvl(self, lvl):
        self.stats['lvl'] += lvl
        self.stats['hp_max'] += lvl*40
        self.stats['hp'] = self.stats['hp_max']
        self.stats['attack_pwr'] += lvl*5
        self.stats['mp_max'] += lvl*80
        self.stats['mp'] = self.stats['mp_max']
        self.stats['exp_to_lvl'] += 170

    def hp_bar(self):
        return int( self.stats['hp'] / self.stats['hp_max'] * 300 )

    def mp_bar(self):
        return int( self.stats['mp'] / self.stats['mp_max'] * 300 )
    def exp_bar(self):
        return int( self.stats['exp'] / self.stats['exp_to_lvl'] * 300 )

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