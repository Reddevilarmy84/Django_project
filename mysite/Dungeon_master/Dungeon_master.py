import os
import json
import random

path_to_json_DM = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Dungeon_master.json')

mob_content_list = [
    {
        'class': 'Пещерная крыса',
        'img': 'main/img/mob/mob_0.jpg',
        'spec1': 'укус крысы',
        'spec2': 'удар хвостом',
        'spec3': 'яростные когти',
        'spec0_img': 'main/img/mob/mob_0/spec_0.jpg',
        'spec1_img': 'main/img/mob/mob_0/spec_1.jpg',
        'spec2_img': 'main/img/mob/mob_0/spec_2.jpg',
        'spec3_img': 'main/img/mob/mob_0/spec_3.jpg',
    },
    {
        'class': 'Гном',
        'img': 'main/img/mob/mob_1.jpg',
        'spec1': 'удар дубиной',
        'spec2': 'Бросок камнем',
        'spec3': 'Яростный удар',
        'spec0_img': 'main/img/mob/mob_1/spec_0.jpg',
        'spec1_img': 'main/img/mob/mob_1/spec_1.jpg',
        'spec2_img': 'main/img/mob/mob_1/spec_2.jpg',
        'spec3_img': 'main/img/mob/mob_1/spec_3.jpg',
    },
    {
        'class': 'Пещерный волк',
        'img': 'main/img/mob/mob_2.jpg',
        'spec1': 'укус волка',
        'spec2': 'удар лапой',
        'spec3': 'Удар хвостом',
        'spec0_img': 'main/img/mob/mob_2/spec_0.jpg',
        'spec1_img': 'main/img/mob/mob_2/spec_1'
                     '.jpg',
        'spec2_img': 'main/img/mob/mob_2/spec_2.jpg',
        'spec3_img': 'main/img/mob/mob_2/spec_3.jpg',
    },
]

mob_stats_list = [
    {
        'lvl': 1,
        'attack_pwr': 10,
        'hp': 50,
        'hp_max': 50,
        'hp_before': 50,
        'mp': 100,
        'mp_max': 100,
        'mp_before': 100,
        'exp': 100,
        'exp_to_lvl': 100,
        'exp_before': 0,
        'spec1_pwr': 20,
        'spec2_pwr': 30,
        'spec3_pwr': 40,
        'spec1_mp': 20,
        'spec2_mp': 30,
        'spec3_mp': 40,
    },
    {
        'lvl': 1,
        'attack_pwr': 10,
        'hp': 50,
        'hp_max': 50,
        'hp_before': 50,
        'mp': 100,
        'mp_max': 100,
        'mp_before': 100,
        'exp': 100,
        'exp_to_lvl': 100,
        'exp_before': 0,
        'spec1_pwr': 20,
        'spec2_pwr': 30,
        'spec3_pwr': 40,
        'spec1_mp': 20,
        'spec2_mp': 30,
        'spec3_mp': 40,
    },
    {
        'lvl': 1,
        'attack_pwr': 10,
        'hp': 50,
        'hp_max': 50,
        'hp_before': 50,
        'mp': 100,
        'mp_max': 100,
        'mp_before': 100,
        'exp': 100,
        'exp_to_lvl': 100,
        'exp_before': 0,
        'spec1_pwr': 20,
        'spec2_pwr': 30,
        'spec3_pwr': 40,
        'spec1_mp': 20,
        'spec2_mp': 30,
        'spec3_mp': 40,
    },
]
class Game:
    def __init__(self):
        self.game = False


class Mob:
    current_attack = {'name': 'продолжить'}
    content = {}
    stats = {}

    def set_mob(self):
        self.content = random.choice(mob_content_list)
        print(mob_content_list.index(self.content))
        self.stats = mob_stats_list[mob_content_list.index(self.content)]
        print(self.content)

    def set_lvl_mob(self, lvl):
        lvl = lvl if lvl > 0 else 1
        for i in range(1, lvl + 1):
            self.stats = {k: int(v * 1.2) for k, v in self.stats.items()}
        self.stats['lvl'] += lvl
        self.stats['hp'] = self.stats['hp_max']
        self.stats['mp'] = self.stats['mp_max']

    def attack(self, num):
        keys = ['id', 'pwr', 'name', 'img', 'mp_before', 'mp']
        if num != 0 and self.stats['mp'] >= self.stats[f'spec{num}_mp']:
            values = [num, self.stats[f'spec{num}_pwr'], self.content[f'spec{num}'], self.content[f'spec{num}_img'], self.stats['mp'], self.stats['mp']-self.stats[f'spec{num}_mp']]
            print('Спец атака')
        else:
            values = [0, self.stats[f'attack_pwr'], 'Атака', self.content['spec0_img'],
                      self.stats['mp'], self.stats['mp']]
            print('обычная атака')
        self.current_attack = dict(zip(keys, values))
        print(self.current_attack)
        self.stats['mp'] = self.current_attack['mp']



    def hp_bar(self):
        return 65 if int(self.stats['hp'] / self.stats['hp_max'] * 300) <= 65 else int(self.stats['hp'] / self.stats['hp_max'] * 300)

    def mp_bar(self):
        return 65 if int(self.stats['mp'] / self.stats['mp_max'] * 300) <= 65 else int(self.stats['mp'] / self.stats['mp_max'] * 300)

    def exp_bar(self):
        return 65 if int(self.stats['exp'] / self.stats['exp_to_lvl'] * 300) <= 65 else int(self.stats['exp'] / self.stats['exp_to_lvl'] * 300)


class Hero:
    current_attack = {}
    content = {}
    stats = {}
    stats_list = [
        {
            'lvl': 1,
            'attack_pwr': 10,
            'hp': 100,
            'hp_max': 100,
            'hp_before': 50,
            'mp': 300,
            'mp_max': 300,
            'mp_before': 100,
            'exp': 0,
            'exp_to_lvl': 100,
            'exp_before': 0,
            'spec1_pwr': 20,
            'spec2_pwr': 30,
            'spec3_pwr': 40,
            'spec1_mp': 20,
            'spec2_mp': 30,
            'spec3_mp': 40,
        },
        {
            'lvl': 1,
            'attack_pwr': 10,
            'hp': 300,
            'hp_max': 300,
            'hp_before': 50,
            'mp': 100,
            'mp_max': 100,
            'mp_before': 100,
            'exp': 0,
            'exp_to_lvl': 100,
            'exp_before': 0,
            'spec1_pwr': 20,
            'spec2_pwr': 30,
            'spec3_pwr': 40,
            'spec1_mp': 20,
            'spec2_mp': 30,
            'spec3_mp': 40,
        },
        {
            'lvl': 1,
            'attack_pwr': 10,
            'hp': 200,
            'hp_max': 200,
            'hp_before': 200,
            'mp': 200,
            'mp_max': 200,
            'mp_before': 200,
            'exp': 0,
            'exp_to_lvl': 100,
            'exp_before': 0,
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
            'name': 'Магнус',
            'class': 'маг',
            'img': 'main/img/hero/hero_0.jpg',
            'spec1': 'огненный шар',
            'spec2': 'ледяной шторм',
            'spec3': 'солнечная вспышка',
            'spec0_img': 'main/img/hero/hero_0/spec_0.jpg',
            'spec1_img': 'main/img/hero/hero_0/spec_1.jpg',
            'spec2_img': 'main/img/hero/hero_0/spec_2.jpg',
            'spec3_img': 'main/img/hero/hero_0/spec_3.jpg',
        },
        {
            'name': 'Ахилес',
            'class': 'воин',
            'img': 'main/img/hero/hero_1.jpg',
            'spec1': 'рассечение',
            'spec2': 'выпад силы',
            'spec3': 'снизхождение',
            'spec0_img': 'main/img/hero/hero_1/spec_0.jpg',
            'spec1_img': 'main/img/hero/hero_1/spec_1.jpg',
            'spec2_img': 'main/img/hero/hero_1/spec_2.jpg',
            'spec3_img': 'main/img/hero/hero_1/spec_3.jpg',
        },
        {
            'name': 'Раймонд',
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
        exp_before = self.stats['exp']
        for i in range(1, lvl+1):
            self.stats = {k:int(v*1.2) for k, v in self.stats.items()}
        self.stats['lvl'] += lvl
        self.stats['hp'] = self.stats['hp_max']
        self.stats['mp'] = self.stats['mp_max']
        self.stats['exp'] = exp_before

    def choose_hero(self, num):
        self.stats = self.stats_list[num]
        self.content = self.content_list[num]
        self.stats['hp'] = self.stats['hp_max']
        self.stats['mp'] = self.stats['mp_max']
        self.stats['exp'] = 0

    def attack(self, num):
        keys = ['id', 'pwr', 'name', 'img', 'mp_before', 'mp']
        if num != 0 and self.stats['mp'] >= self.stats[f'spec{num}_mp']:
            values = [num, self.stats[f'spec{num}_pwr'], self.content[f'spec{num}'], self.content[f'spec{num}_img'], self.stats['mp'], self.stats['mp']-self.stats[f'spec{num}_mp']]
            print('Спец атака')
        else:
            values = [0, self.stats[f'attack_pwr'], 'Атака', None,
                      self.stats['mp'], self.stats['mp']]
            print('обычная атака')
        self.current_attack = dict(zip(keys, values))
        print(self.current_attack)
        self.stats['mp'] = self.current_attack['mp']

    def hp_bar(self):
        return 60 if int( self.stats['hp'] / self.stats['hp_max'] * 300 ) <= 60 else int( self.stats['hp'] / self.stats['hp_max'] * 300 )

    def mp_bar(self):
        return 60 if int( self.stats['mp'] / self.stats['mp_max'] * 300 ) <= 60 else int( self.stats['mp'] / self.stats['mp_max'] * 300 )

    def exp_bar(self):
        return 90 if int( self.stats['exp'] / self.stats['exp_to_lvl'] * 300 ) <= 90 else int( self.stats['exp'] / self.stats['exp_to_lvl'] * 300 )


class Location:
    content = {'img': 'main/img/locations/loc_0.jpg'}
    stats = {

    }
    content_list = [
        {
            'name': 'Пещера пиратов',
            'img': 'main/img/locations/loc_1.jpg',
        },
        {
            'name': 'Пещера троля',
            'img': 'main/img/locations/loc_2.jpg',
        },
        {
            'name': 'Сумеречная пещера',
            'img': 'main/img/locations/loc_3.jpg',
        },

    ]
    stats_list = [
        {
            'length': 10,
            'completed': 0,
            'chance_mob': 20,
            'chance_reward': 20,
            'dificult': 0,
        },
        {
            'length': 15,
            'completed': 0,
            'chance_mob': 30,
            'chance_reward': 30,
            'dificult': 1,
        },
        {
            'length': 20,
            'completed': 0,
            'chance_mob': 50,
            'chance_reward': 50,
            'dificult': 2,
        },

    ]


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