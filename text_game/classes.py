import math


class Cfg:
    sleep = 0
    sleep_walk = 0


class Colors:
    black = '\033[30m'
    red =  '\033[31m'
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

    res = '\033[0m' #сброс
    bolt = '\033[1m' #жирный
    light = '\033[2m' #Блёклый
    curs = '\033[3m' #Курсив
    line = '\033[4m' #Подчёркнутый
    blink = '\033[5m' # Редкое мигание
    blink_fast = '\033[6m' # Частое мигание
    inv = '\033[7m' # Смена цвета фона с цветом текста
    tab = "                               "


class Mob:
    exp = 10
    mp = 30
    location = ''
    hp = 30
    pwr = 10
    name = 'кто-то'
    lvl = 1
    gold_min = 1
    gold_max = 1000

    def __init__(self, **kwargs):
        if 'pwr' in kwargs:
            self.pwr = kwargs['pwr']
        if 'name' in kwargs:
            self.name = kwargs['name']


    def up_lvl(self, lvl):
        self.pwr = lvl*2
        self.lvl = lvl
        self.exp = 50 + lvl*50
        self.hp = lvl*50
        self.mp = lvl*30

    def mhp(self, lvl):
        self.hp = lvl*40


    def locate(self, loc):
        self.location = loc


class Hero:
    exp = 0
    exp_to_lvl = 70
    lvl=1
    type= 'хз кто'
    hp = 300
    hp_max = 300
    mp = 100
    mp_max = 100
    crit = 30
    m_crit = 10
    m_pwr = 15
    pmoney = 0
    frags = 0
    heal_max = 50
    pwr = 10
    name = 'ХЗ как звать'

    spec1 = 'огненный шар'
    spec1_mp = 20
    spec1_lvl = 1
    spec1_pwr = 0

    spec2 = 'огненный шторм'
    spec2_mp = 30
    spec2_lvl = 1
    spec2_pwr = 0

    spec3 = 'плазменный взрыв'
    spec3_mp = 50
    spec3_lvl = 1
    spec3_pwr = 0

    spec = [spec1, spec2, spec3]
    def __init__(self, **kwargs):
        if 'type' in kwargs:
            self.type = kwargs['type']
        if 'lvl' in kwargs:
            self.lvl = kwargs['lvl']
        if 'name' in kwargs:
            self.name = kwargs['name']

    def php(self, set_hp):
        self.hp += set_hp

    def heal(self, heal_maxx):
        self.heal_max = heal_maxx

    def frag(self, frag):
        self.frags +=frag

    def money(self, money):
        self.pmoney += money


    def up_lvl(self, lvl):
        self.lvl += lvl
        self.hp_max += lvl*40
        self.hp = self.hp_max
        self.pwr += lvl*5
        self.m_pwr += lvl*2
        self.mp_max += lvl * 20
        self.mp = self.mp_max

        self.crit += lvl*1
        self.m_crit += lvl*2
        self.exp_to_lvl += 110
        self.heal_max += lvl*5

        self.spec1_lvl = math.floor(self.lvl/2)
        self.spec1_pwr = math.floor(self.lvl/2) * 9
        self.spec1_mp += (lvl * 10)

        self.spec2_mp += lvl * 14
        self.spec2_lvl = math.floor(self.lvl/5)
        self.spec2_pwr = math.floor(self.lvl/5) * 38

        self.spec3_mp += lvl * 19
        self.spec3_lvl = math.floor(self.lvl/10)
        self.spec3_pwr = math.floor(self.lvl/10) * 147

    def info(self):
        grey_inv = Colors.grey + Colors.inv
        print('')
        print(grey_inv + self.name, self.type, self.lvl, 'уровня.' + ' '*51 + Colors.res)
        print(grey_inv + 'HP:', self.hp_max, ' '*62, Colors.res)
        print(grey_inv + 'MP:', self.mp_max, ' '*62, Colors.res)
        print(grey_inv, end='Спецприемы: ')
        print(grey_inv + self.spec1, self.spec1_lvl, 'ур.', 'Мощность:',
              self.spec1_pwr, '.', 'Стоит:', self.spec1_mp, 'MP.', ' '*7, Colors.res)
        print(grey_inv + ' '*len('Спецприемы: ') + self.spec2,
              self.spec2_lvl, 'ур.', 'Мощность:',
              self.spec2_pwr, '.', 'Стоит:', self.spec2_mp, 'MP.', ' '*2, Colors.res)
        print(grey_inv + ' ' * len('Спецприемы: ') + self.spec3,
              self.spec3_lvl, 'ур.', 'Мощность:',
              self.spec3_pwr, '.', 'Стоит:', self.spec3_mp, 'MP.', Colors.res)
        print(grey_inv + 'Физическая атака', self.pwr,
              'Критический удар', math.floor(self.crit), ' '*30, Colors.res)
        print(grey_inv + 'Магическая атака', self.m_pwr,
              'Критическая удар', math.floor(self.m_crit), ' '*30, Colors.res)

    def info_spec(self, spec):
        specs = [self.spec1_lvl, self.spec2_lvl, self.spec3_lvl]
        specv = specs[spec]
        return(specv)


class Loc:
    locs = ['Мрачный лес', 'Древняя роща', 'Загадочная пещера', 'Поле брани']
    loc_from = ['Лесной', 'Кустарный', 'Пещерный', 'Полевой']
    enemy_meet = 15
    leght_max = 1000  # максимальная длина локации в метрах
    leght_min = 100  # минимальная длина локации с метрах
    walk_step = 1  # шаг прохождения локации в метрах


class Forest:
    name = 'Мрачный лес'
    mobs = ['Лесной дракон', 'Тролль', 'Эльф', 'Ведьма']


class Loot:
    win_list = ['матрешку', 'телевизор', 'шапку-ушанку', 'Ааавтомобииль!', 'пачку семечек', 'карманный фонарик', 'чебурек с мясом', 'глаз единорога']
    loose_list = ['зубы', 'совесть', 'трусы', 'надежду', 'одежду']
    currency = ['RUB']


class Kung_fu:
    pass

spec_player2 = ['волшебный пендель', 'молниеносный лещ', 'смачный апперкот']
weapons = ['достает из кармана банан', 'берет в руки лопату', 'наматывает на руку цепь', 'снимает сапог', 'снимает с правой ноги протез', 'надувает резиновую бабу']
atack_part = ['сносит колено', 'пробивает челлюсть', 'ломает нос', 'бьет по голове', 'попадает в пах', 'наносит удар по солнечному сплетению']