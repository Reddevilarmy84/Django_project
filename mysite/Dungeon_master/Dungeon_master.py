import os
import json
import random
import datetime

path_to_json_DM = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Dungeon_master.json')


class Game:
    def __init__(self):
        self.phase = 'title'
        self.action = None
        self.now = datetime.datetime.now()
    def date_time(self):
        return self.now.strftime("%d/%m/%Y %H:%M")

    def __repr__(self):
        return f"Game(phase={self.phase}, action={self.action}, now={self.now})"

class Mob:
    current_attack = {}
    content = {}
    stats = {}
    content_list = [
        {
            'name': 'Пещерная крыса',
            'img': 'main/img/mob/mob_0/mob.jpg',
            'spec1': 'Укус крысы',
            'spec2': 'Яростные когти',
            'spec3': 'Чума',
            'spec0_img': 'main/img/mob/mob_0/spec_0.jpg',
            'spec1_img': 'main/img/mob/mob_0/spec_1.jpg',
            'spec2_img': 'main/img/mob/mob_0/spec_2.jpg',
            'spec3_img': 'main/img/mob/mob_0/spec_3.jpg',
        },
        {
            'name': 'Дикий кот',
            'img': 'main/img/mob/mob_1/mob.jpg',
            'spec1': 'Цап царап',
            'spec2': 'Кусь',
            'spec3': 'Смертельный прыжок',
            'spec0_img': 'main/img/mob/mob_1/spec_0.jpg',
            'spec1_img': 'main/img/mob/mob_1/spec_1.jpg',
            'spec2_img': 'main/img/mob/mob_1/spec_2.jpg',
            'spec3_img': 'main/img/mob/mob_1/spec_3.jpg',
        },
        {
            'name': 'Пещерный волк',
            'img': 'main/img/mob/mob_2/mob.jpg',
            'spec1': 'Клыки',
            'spec2': 'Разящие лапы',
            'spec3': 'Ярость волка',
            'spec0_img': 'main/img/mob/mob_2/spec_0.jpg',
            'spec1_img': 'main/img/mob/mob_2/spec_1.jpg',
            'spec2_img': 'main/img/mob/mob_2/spec_2.jpg',
            'spec3_img': 'main/img/mob/mob_2/spec_3.jpg',
        },
        {
            'name': 'Горный гном',
            'img': 'main/img/mob/mob_3/mob.jpg',
            'spec1': 'Получи дубиной!',
            'spec2': 'Камень летит!',
            'spec3': 'Разозлил гнома!',
            'spec0_img': 'main/img/mob/mob_3/spec_0.jpg',
            'spec1_img': 'main/img/mob/mob_3/spec_1.jpg',
            'spec2_img': 'main/img/mob/mob_3/spec_2.jpg',
            'spec3_img': 'main/img/mob/mob_3/spec_3.jpg',
        },        {
            'name': 'Изумрудный змей',
            'img': 'main/img/mob/mob_4/mob.jpg',
            'spec1': 'удар хвостом',
            'spec2': 'Нейротоксин',
            'spec3': 'Удушение',
            'spec0_img': 'main/img/mob/mob_4/spec_0.jpg',
            'spec1_img': 'main/img/mob/mob_4/spec_1.jpg',
            'spec2_img': 'main/img/mob/mob_4/spec_2.jpg',
            'spec3_img': 'main/img/mob/mob_4/spec_3.jpg',
        },        {
            'name': 'Носферату',
            'img': 'main/img/mob/mob_5/mob.jpg',
            'spec1': 'Острое крыло',
            'spec2': 'Укус в шею',
            'spec3': 'Иди на ручки!',
            'spec0_img': 'main/img/mob/mob_5/spec_0.jpg',
            'spec1_img': 'main/img/mob/mob_5/spec_1.jpg',
            'spec2_img': 'main/img/mob/mob_5/spec_2.jpg',
            'spec3_img': 'main/img/mob/mob_5/spec_3.jpg',
        },        {
            'name': 'Папоротник- мутант',
            'img': 'main/img/mob/mob_6/mob.jpg',
            'spec1': 'Острые шипы',
            'spec2': 'Ядовитый бутон',
            'spec3': 'Соцветие смерти',
            'spec0_img': 'main/img/mob/mob_6/spec_0.jpg',
            'spec1_img': 'main/img/mob/mob_6/spec_1.jpg',
            'spec2_img': 'main/img/mob/mob_6/spec_2.jpg',
            'spec3_img': 'main/img/mob/mob_6/spec_3.jpg',
        },        {
            'name': 'Древень',
            'img': 'main/img/mob/mob_7/mob.jpg',
            'spec1': 'разящие ветки',
            'spec2': 'Ядовитые споры',
            'spec3': 'Проростание',
            'spec0_img': 'main/img/mob/mob_7/spec_0.jpg',
            'spec1_img': 'main/img/mob/mob_7/spec_1.jpg',
            'spec2_img': 'main/img/mob/mob_7/spec_2.jpg',
            'spec3_img': 'main/img/mob/mob_7/spec_3.jpg',
        },        {
            'name': 'Водяной элементаль',
            'img': 'main/img/mob/mob_8/mob.jpg',
            'spec1': 'Кинетический удар',
            'spec2': 'Накрыло волной',
            'spec3': 'Водоворот',
            'spec0_img': 'main/img/mob/mob_8/spec_0.jpg',
            'spec1_img': 'main/img/mob/mob_8/spec_1.jpg',
            'spec2_img': 'main/img/mob/mob_8/spec_2.jpg',
            'spec3_img': 'main/img/mob/mob_8/spec_3.jpg',
        },
    ]
    stats_list = [
        {
            # 'class': 'Пещерная крыса',
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
            'spec1_pwr': 15,
            'spec2_pwr': 20,
            'spec3_pwr': 30,
            'spec1_mp': 20,
            'spec2_mp': 30,
            'spec3_mp': 40,
        },
        {
            # 'class': 'Дикий кот',
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
            'spec1_pwr': 15,
            'spec2_pwr': 20,
            'spec3_pwr': 30,
            'spec1_mp': 20,
            'spec2_mp': 30,
            'spec3_mp': 40,
        },
        {
            # 'class': 'Пещерный волк',
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
            'spec1_pwr': 15,
            'spec2_pwr': 20,
            'spec3_pwr': 30,
            'spec1_mp': 20,
            'spec2_mp': 30,
            'spec3_mp': 40,
        },
        {
            # 'class': 'Горный гном',
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
            'spec1_pwr': 15,
            'spec2_pwr': 20,
            'spec3_pwr': 30,
            'spec1_mp': 20,
            'spec2_mp': 30,
            'spec3_mp': 40,
        },
        {
            # 'class': 'Изумрудный змей',
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
            'spec1_pwr': 15,
            'spec2_pwr': 20,
            'spec3_pwr': 30,
            'spec1_mp': 20,
            'spec2_mp': 30,
            'spec3_mp': 40,
        },
        {
            # 'class': 'Носферату',
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
            'spec1_pwr': 15,
            'spec2_pwr': 20,
            'spec3_pwr': 30,
            'spec1_mp': 20,
            'spec2_mp': 30,
            'spec3_mp': 40,
        },
        {
            # 'class': 'Папоротник- мутант',
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
            'spec1_pwr': 15,
            'spec2_pwr': 20,
            'spec3_pwr': 30,
            'spec1_mp': 20,
            'spec2_mp': 30,
            'spec3_mp': 40,
        },
        {
            # 'class': 'Древень',
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
            'spec1_pwr': 15,
            'spec2_pwr': 20,
            'spec3_pwr': 30,
            'spec1_mp': 20,
            'spec2_mp': 30,
            'spec3_mp': 40,
        },
        {
            # 'class': 'Водяной элементаль',
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
            'spec1_pwr': 15,
            'spec2_pwr': 20,
            'spec3_pwr': 30,
            'spec1_mp': 20,
            'spec2_mp': 30,
            'spec3_mp': 40,
        },
    ]

    def set_mob(self, mobs: list = None):
        print(mobs)
        start = mobs[0] if mobs else None
        end = mobs[1] if mobs else None
        self.content = dict(random.choice(self.content_list[start:end]).items())
        self.stats = dict(self.stats_list[self.content_list.index(self.content)].items())

    def set_lvl_mob(self, lvl: int):
        lvl_before = self.stats['lvl']
        for i in range(1, lvl + 1):
            self.stats = {k: int(v+(v*0.25)) for k, v in self.stats.items()}
        self.stats['lvl'] = lvl_before + lvl


    def attack(self, num):
        keys = ['pwr', 'name', 'img', 'mp_before', 'mp']
        if num and self.stats['mp'] >= self.stats[f'spec{num}_mp']:
            values = [self.stats[f'spec{num}_pwr'], self.content[f'spec{num}'], self.content[f'spec{num}_img'], self.stats['mp'], self.stats['mp']-self.stats[f'spec{num}_mp']]
        else:
            values = [self.stats[f'attack_pwr'], 'Атака', self.content['spec0_img'],
                      self.stats['mp'], self.stats['mp']]
        self.current_attack = dict(zip(keys, values))
        self.stats['mp'] = self.current_attack['mp']


    def hp_bar(self):
        return 65 if int(self.stats['hp'] / self.stats['hp_max'] * 300) <= 65 else int(self.stats['hp'] / self.stats['hp_max'] * 300)


    def mp_bar(self):
        return 65 if int(self.stats['mp'] / self.stats['mp_max'] * 300) <= 65 else int(self.stats['mp'] / self.stats['mp_max'] * 300)

    def half_damage_pwr(self):
        return int(self.current_attack['pwr']/2)

class Hero:
    current_attack = {}
    content = {}
    potions = {'heal': 0, 'mana': 0, 'fury': 0, 'shield': 0, 'spikes': 0, 'gold': 0}
    condition = {'heal': False, 'mana': False, 'fury': False, 'shield': False, 'spikes': False}
    stats = {
            'lvl': 1,
            'attack_pwr': 10,
            'hp': 200,
            'hp_max': 200,
            'hp_before': 200,
            'mp': 500,
            'mp_max': 500,
            'mp_before': 500,
            'exp': 0,
            'exp_to_lvl': 200,
            'exp_before': 0,
            'spec1_pwr': 20,
            'spec2_pwr': 30,
            'spec3_pwr': 40,
            'spec1_mp': 22,
            'spec2_mp': 35,
            'spec3_mp': 48,
        }
    stats_list = [
        {
            'lvl': 1,
            'attack_pwr': 25,
            'hp': 300,
            'hp_max': 300,
            'hp_before': 300,
            'mp': 200,
            'mp_max': 200,
            'mp_before': 200,
            'exp': 0,
            'exp_to_lvl': 200,
            'exp_before': 0,
            'spec1_pwr': 35,
            'spec2_pwr': 60,
            'spec3_pwr': 100,
            'spec1_mp': 22,
            'spec2_mp': 35,
            'spec3_mp': 48,
        },
        {
            'lvl': 1,
            'attack_pwr': 40,
            'hp': 400,
            'hp_max': 400,
            'hp_before': 400,
            'mp': 150,
            'mp_max': 150,
            'mp_before': 150,
            'exp': 0,
            'exp_to_lvl': 200,
            'exp_before': 0,
            'spec1_pwr': 40,
            'spec2_pwr': 50,
            'spec3_pwr': 80,
            'spec1_mp': 18,
            'spec2_mp': 25,
            'spec3_mp': 38,
        },
        {
            'lvl': 1,
            'attack_pwr': 25,
            'hp': 300,
            'hp_max': 300,
            'hp_before': 300,
            'mp': 200,
            'mp_max': 200,
            'mp_before': 200,
            'exp': 0,
            'exp_to_lvl': 200,
            'exp_before': 0,
            'spec1_pwr': 35,
            'spec2_pwr': 60,
            'spec3_pwr': 100,
            'spec1_mp': 22,
            'spec2_mp': 35,
            'spec3_mp': 48,
        },
]

    content_list = [
        {
            'name': 'Магнус',
            'class': 'Маг стихий',
            'img': 'main/img/hero/hero_0.jpg',
            'spec1': 'Огненный шар',
            'spec2': 'Ледяной шторм',
            'spec3': 'Солнечная вспышка',
            'spec0_img': 'main/img/hero/hero_0/spec_0.jpg',
            'spec1_img': 'main/img/hero/hero_0/spec_1.jpg',
            'spec2_img': 'main/img/hero/hero_0/spec_2.jpg',
            'spec3_img': 'main/img/hero/hero_0/spec_3.jpg',
        },
        {
            'name': 'Артур',
            'class': 'Доблестный рыцарь',
            'img': 'main/img/hero/hero_1.jpg',
            'spec1': 'Удар щитом',
            'spec2': 'Ярость',
            'spec3': 'Неистовость',
            'spec0_img': 'main/img/hero/hero_1/spec_0.jpg',
            'spec1_img': 'main/img/hero/hero_1/spec_1.jpg',
            'spec2_img': 'main/img/hero/hero_1/spec_2.jpg',
            'spec3_img': 'main/img/hero/hero_1/spec_3.jpg',
        },
        {
            'name': 'Денгар',
            'class': 'Теневой страж',
            'img': 'main/img/hero/hero_2.jpg',
            'spec1': 'Стремительный кинжал',
            'spec2': 'Выстрел из лука',
            'spec3': 'Атака тени',
            'spec0_img': 'main/img/hero/hero_2/spec_0.jpg',
            'spec1_img': 'main/img/hero/hero_2/spec_1.jpg',
            'spec2_img': 'main/img/hero/hero_2/spec_2.jpg',
            'spec3_img': 'main/img/hero/hero_2/spec_3.jpg',
        },
    ]

    def up_lvl(self, lvl):
        exp_before = self.stats['exp']
        lvl_before = self.stats['lvl']
        for i in range(1, lvl+1):
            self.stats = {k:int(v+(v*0.24)) for k, v in self.stats.items()}
        self.stats['lvl'] = lvl_before + lvl
        self.stats['exp'] = exp_before
        self.stats['exp_to_lvl'] = int(self.stats['exp_to_lvl']*1.3)
        self.stats['hp'] = self.stats['hp_max']
        self.stats['mp'] = self.stats['mp_max']

    def choose_hero(self, num):
        self.stats = dict(self.stats_list[num].items())
        self.content = dict(self.content_list[num].items())

    def attack(self, num):
        keys = ['pwr', 'name', 'img', 'mp_before', 'mp']
        if num and self.stats['mp'] >= self.stats[f'spec{num}_mp']:
            values = [self.stats[f'spec{num}_pwr'], self.content[f'spec{num}'], self.content[f'spec{num}_img'], self.stats['mp'], self.stats['mp']-self.stats[f'spec{num}_mp']]
        else:
            values = [self.stats[f'attack_pwr'], 'Атака', None,
                      self.stats['mp'], self.stats['mp']]
        self.current_attack = dict(zip(keys, values))
        self.stats['mp'] = self.current_attack['mp']

    def hp_bar(self):
        try:
            bar = 70 if int(self.stats['hp'] / self.stats['hp_max'] * 300) <= 70 else int(self.stats['hp'] / self.stats['hp_max'] * 300)
        except:
            bar = 70
        return bar

    def mp_bar(self):
        return 70 if int(self.stats['mp'] / self.stats['mp_max'] * 300) <= 70 else int(self.stats['mp'] / self.stats['mp_max'] * 300)

    def exp_bar(self):
        return 75 if int(self.stats['exp'] / self.stats['exp_to_lvl'] * 300) <= 75 else int(self.stats['exp'] / self.stats['exp_to_lvl'] * 300)

    def exp_bar_value(self):
        return int(self.stats['exp'] / self.stats['exp_to_lvl'] * 100)

    def fury_damage(self):
        return int(self.current_attack['pwr']*1.3)

class Location:
    content = {'img': f'main/img/locations/loc_1.jpg'}
    stats = {}
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
            'length': 20,
            'completed': 0,
            'chance_mob': 20,
            'chance_reward': 20,
            'dificult': 0,
            'mobs_list':[0, 3],
        },
        {
            'length': 35,
            'completed': 0,
            'chance_mob': 30,
            'chance_reward': 30,
            'dificult': 1,
            'mobs_list': [3, 6],
        },
        {
            'length': 50,
            'completed': 0,
            'chance_mob': 50,
            'chance_reward': 50,
            'dificult': 2,
            'mobs_list': [6, 9],
        },

    ]
    step_discription = {}
    step_discriptions = [
        {
            'discription': 'Здесь ничего нет'
        },
        {
            'discription': 'Пустота да мрак'
        },
        {
            'discription': 'За углом кто-то есть?'
        },
        {
            'discription': 'Холодно, тихо.. Что это за хруст?'
        },
        {
            'discription': 'Здесь всё чисто!'
        },
        {
            'discription': 'Продвигаюсь вперёд.'
        },
        {
            'discription': 'В животе урчит, не отказался бы от Дошика.'
        },
        {
            'discription': 'Подозрительно тихо!'
        },
        {
            'discription': 'Такое чувство, что за мной кто-то следит.'
        },
    ]

class Loot:
    loot = [
        {
            'name': 'heal',
            'img': "main/img/items/potion_0.jpg",
            'quantity': 1,
        },
        {
            'name': 'mana',
            'img': "main/img/items/potion_1.jpg",
            'quantity': 1,
        },
        {
            'name': 'fury',
            'img': "main/img/items/potion_2.jpg",
            'quantity': 1,
        },
        {
            'name': 'shield',
            'img': 'main/img/items/potion_3.jpg',
            'quantity': 1,
        },
        {
            'name': 'spikes',
            'img': 'main/img/items/potion_4.jpg',
            'quantity': 1,
        },
        {
            'name': 'gold',
            'img': 'main/img/items/gold.jpg',
            'quantity': 200,
        },
    ]
    bount = []
    def bounty(self, luck: int = 0):
        self.bount.clear()
        # шанс получить зелье лечения или маны
        if random.randrange(100) < 40 + luck:
            self.bount.append(random.choice(self.loot[0:2]))
        # шанс получить зелье ярости
        if random.randrange(100) < 25 + luck:
            self.bount.append(random.choice(self.loot[2:3]))
        # шанс получить зелье щита или шипов
        if random.randrange(100) < 10 + luck:
            self.bount.append(random.choice(self.loot[3:5]))
        # шанс получить золото
        if random.randrange(100) < 70 + luck:
            gold = self.loot[5]
            gold['quantity'] = random.randrange(500)
            self.bount.append(gold)

def mob_spec_chance(chance):
    n = random.randrange(1, 100)
    n = n + chance if n + chance < 100 else 100
    return 1 if 50 < n < 75 else 2 if 74 < n < 90 else 3 if 89 < n < 100 else 0

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