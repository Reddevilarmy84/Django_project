from classes import Hero, Mob, Loc, Cfg, Loot
player = Hero(type='Маг', name = 'Валера')
enemy = Mob(name = 'Дрозд', pwr = 5)
import math, time
from classes import Colors as c
from random import randint as rand

def p_critical():
    chance = rand(1, 100)
    if chance <= player.crit:
        var = rand(1, 3)
        if var == 1:
            mult = 2
            txt = 'CRITICAL HIT! x2 '
        if var == 2:
            mult = 3
            txt = 'CRITICAL HIT! x3 '
        if var == 3:
            mult = 5
            txt = 'CRITICAL HIT! x5 '
    else:
        mult = 1
        txt = ''
    return(mult, txt)


def m_critical():
    chance = rand(1, 100)
    if chance <= player.crit:
        var = rand(1, 2)
        if var == 1:
            mult = 2
            txt = 'CRITICAL HIT! x2 '
        if var == 2:
            mult = 3
            txt = 'CRITICAL HIT! x3 '
        if var == 3:
            mult = 5
            txt = 'CRITICAL HIT! x5 '
    else:
        mult = 1
        txt = ''
    return(mult, txt)


def heal(lvl):
    if player.heal_max < 0:
        player.heal(0)
    heal = rand(0, player.heal_max)
    return(heal)


def win_loot_gen():
    how_much = rand(enemy.gold_min, enemy.gold_max)
    cur = Loot.currency[rand(0, len(Loot.currency) - 1)]
    loot1 = (str(how_much) + ' ' + str(cur))
    loot2 = Loot.win_list[rand(0, len(Loot.win_list) - 1)]
    loot3 = Loot.win_list[rand(0, len(Loot.win_list) - 2)]

    return (loot1, loot2, loot3, how_much)


def loose_loot_gen():
    loot = Loot.loose_list[rand(0, len(Loot.loose_list) - 1)]
    surp = Loot.win_list[rand(0, len(Loot.win_list) - 1)]
    return (loot, surp)


def location_leght_d():
    if Loc.leght_min > Loc.leght_max:
        leght = 100
        print('Установлена стандартная длина локации 100м')
    else:
        leght = rand(Loc.leght_min, Loc.leght_max)
    return(leght)


def enemy_chance():
    randi = rand(1, 100)
    if Loc.enemy_meet < 1:
        Loc.enemy_meet = 1
        print('meet sets on 1')
    elif Loc.enemy_meet > 100:
        Loc.enemy_meet = 100
        print('meet sets on 100')
    else:
        if randi <= Loc.enemy_meet:
            chance = 1
        else:
            chance = 0
        return(chance)


def location_name():
    num = rand(0, len(Loc.locs))
    txt = Loc.loc_from[num - 1]
    enemy.locate(txt)
    return Loc.locs[num - 1]


def enemy_atack():
    from random import randint as rand
    from time import sleep
    from classes import spec_player2 as specs, weapons, atack_part as parts, Colors as c

    spec = specs[rand(0, len(specs) - 1)]
    weapon = weapons[rand(0, len(weapons) - 1)]
    part = parts[rand(0, len(parts) - 1)]
    crit, crit_txt = m_critical()
    damage = enemy.pwr * crit
    print(c.red + c.bolt + enemy.location, enemy.name, 'применяет', spec, 'затем', weapon)
    print('и', part, player.name, 'нанеся', damage, 'урона', crit_txt, c.res)

    sleep(Cfg.sleep)

    return damage


def player_atack():
    from time import sleep
    from classes import weapons, atack_part as parts
    from classes import Colors as c

    g = rand(0, len(player.spec) - 1)
    type = player.spec[g]
    weapon = weapons[rand(0, len(weapons) - 1)]
    part = parts[rand(0, len(parts) - 1)]
    crit, txt = p_critical()

    attack_type = rand(0, 5)
    coast = [player.spec1_mp, player.spec2_mp, player.spec3_mp]
    magic_power = [player.spec1_pwr, player.spec2_pwr, player.spec3_pwr]
    if attack_type != 0 and coast[g] < player.mp:
        damage = (magic_power[g] + player.m_pwr) * crit
        print(c.black + c.bolt + player.name, 'применяет', type, player.info_spec(g), 'LVL')
        print('Поражает ' + enemy.location, enemy.name,
          'нанеся', str(damage), 'урона', c.blue + txt + c.res)
        player.mp -= coast[g]
        print ('потрачено мр:' + str(coast[g]))

    else:
        damage = player.pwr * crit
        print(c.black + c.bolt + player.name, weapon)
        print('и ' + part + ' ' + enemy.location, enemy.name,
          'нанеся', str(damage), 'урона', c.blue + txt + c.res)

    sleep(Cfg.sleep)
    return damage


def avto_battle():
    import time
    from classes import Colors as c

    while player.hp > 0 and enemy.hp > 0:
        a = player_atack()
        enemy.hp -= a
        time.sleep(Cfg.sleep)

        print(c.tab)
        time.sleep(Cfg.sleep)

        if player.hp < 0:
            player.php(0)

        if enemy.hp < 0:
            enemy.hp = 0

        if enemy.hp > 0:
            m_damage = enemy_atack()
            time.sleep(Cfg.sleep)

            player.php(-m_damage)

            time.sleep(Cfg.sleep)

            if player.hp < 0:
                player.hp = 0

            if enemy.hp < 0:
                enemy.hp = 0
        print(' ')
        tabtab = ' ' * (32 - len(str(player.lvl)))
        if player.mp < player.mp_max:
            a = player.mp_max - player.mp #сколько не хватает до макс
            player.mp += player.lvl * 3

            if player.mp >= player.mp_max:
                player.mp = player.mp_max
                print('Восстановлено: ' + str(a), 'MP', 'До максимума')
            else:
                print('Восстановлено: ' + str(player.lvl * 3), 'MP')
        print('')
        print(c.inv + c.bolt + c.green + player.name, player.type,
              player.lvl, 'LVL', c.res + tabtab, c.red,
              c.bolt, c.inv + enemy.location, enemy.name, enemy.lvl,
              'LVL', c.res)
        print(str(hp_bar()))
        print(str(mp_bar()))
        print(str(xp_bar()))
        print('')

        time.sleep(Cfg.sleep)

    return (player.hp, enemy.hp)


def score():
    enemy.up_lvl(player.lvl)
    win1, win2, win3, summa = win_loot_gen()
    print(' ')
    print(c.inv + c.bolt + c.blue + 'Битва начинается!' + c.res)
    print(' ')
    time.sleep(Cfg.sleep)
    tabtab = ' ' * (32 - len(str(player.lvl)))
    print(c.inv + c.bolt + c.green + player.name, player.type,
          player.lvl, 'LVL', c.res + tabtab, c.red,
          c.bolt, c.inv + enemy.location, enemy.name, enemy.lvl,
          'LVL', c.res)
    print(str(hp_bar()))
    print(str(mp_bar()))
    print(str(xp_bar()))
    print(' ')
    time.sleep(Cfg.sleep)
    player.hp, b = avto_battle()
    if player.hp < 0:
        player.hp = 0
    print(' ')
    if player.hp > 0 and b <= 0:
        print(' ')
        print(c.red + enemy.location, enemy.name, c.green + 'повержен!',
              'Получено', c.blue + win1 + ', ' + str(math.floor(enemy.exp)), 'EXP' + c.res)
        player.exp += enemy.exp
        while player.exp >= player.exp_to_lvl:
            player.exp -= player.exp_to_lvl
            player.up_lvl(1)
            enemy.up_lvl(player.lvl)
            print(player.name, 'получает', player.lvl, 'уровень!')
    if player.hp <= 0 and b > 0:
        print(' ')
    if player.hp <= 0 and b <= 0:
        print(' ')
    return (player.hp, summa)


def walk():
    loc = location_name()
    leght = location_leght_d()
    win1, win2, win3, win4 = win_loot_gen()
    loose, surp = loose_loot_gen()
    print(c.bolt + c.green + player.name,
          'попадает в локацию', c.blue + ' ' + loc, c.res)
    time.sleep(Cfg.sleep_walk)
    print(c.green + c.bolt + 'Длина пути', c.blue +
          str(leght), c.green + 'метров', c.res)
    time.sleep(Cfg.sleep_walk)
    i = 0
    while i < leght:
        i += Loc.walk_step
        if player.hp > 0:
            if i >= leght:

                if i > leght:
                    i = leght
                print(c.yellow + c.bolt + 'прошел', c.blue + str(i), c.yellow +
                      'из', c.blue + str(leght), c.yellow + 'метров', c.res)
                print(c.blue + 'локация пройдена!', c.res)
            else:
                print(c.yellow + c.bolt + 'прошел', c.blue + str(i), c.yellow +
                      'из', c.blue + str(leght), c.yellow + 'метров', c.res)
                a = enemy_chance()
                time.sleep(Cfg.sleep_walk)
                if a == 1:
                    print('')
                    print(  c.red + c.inv + c.bolt + 'Путь перегородил',
                            enemy.location, enemy.name, c.res           )
                    time.sleep(Cfg.sleep_walk)
                    enemy.mhp(player.lvl)
                    player.hp, summa = score()
                    if player.hp > 0:
                        player.frag(1)
                        player.money(summa)
                        heal_hp = heal(player.lvl)
                        if heal_hp > 0 and player.hp < player.hp_max and player.hp != player.hp_max:
                            print(  c.green + 'Перевязка ран +', heal_hp,
                                    'здоровья', c.res   )
                            player.hp += heal_hp
                            if player.hp > player.hp_max:
                                player.hp = player.hp_max
                            print(' ')
        else:
            if i > leght:
                i = leght
            print(  c.blue + 'Увы', player.name, 'погиб', 'пройдя',
                  i, 'из', leght, 'метров', c.res  )
            i = leght                           #для остановки цикла шагания по локации
    print(c.red + 'убито мобов', player.frags, c.res)
    if player.hp > 0:
        print(c.green + c.bolt + player.name, c.green + 'получил всего',
              c.blue + str(player.pmoney), c.green + 'рублей', c.green +
              'а так же', c.blue + win2, c.green + 'и', c.blue + win3, c.res)
    else:
        print(c.green + player.name, 'теряет', c.blue + loose, c.green +
              'сохранив', c.blue + str(player.pmoney), c.green + 'рублей')
        print('а так же получает утешительный приз', c.blue + surp, c.res)
    player.info()



def hp_bar():
    from classes import Colors as c
    php = player.hp
    ehp = enemy.hp
    msection = (enemy.lvl*50 / 30)
    psection = (player.hp_max / 30)
    pbar = str( ' ' * int(php / psection + 4 - len(str(player.hp))))
    ebar = str( ' ' * int(ehp / msection + 4 - len(str(enemy.hp))))
    separ = str(' ' * (48 - len(pbar) -len(str(player.hp))))
    if player.hp <= 150 and player.hp> 50:
        bar = c.yellow + c.inv + c.bolt +\
              'HP:' + str(player.hp) + pbar + \
              c.res + separ + c.red + c.inv +\
              'HP:' + str(enemy.hp) + ebar + c.res
    elif player.hp <= 50:
        bar = c.red + c.inv + c.bolt +\
              'HP:' + str(player.hp) + pbar + \
              c.res + separ + c.red + c.inv +\
              'HP:' + str(enemy.hp) + ebar + c.res
    else:
        bar = c.green + c.inv + c.bolt +\
              'HP:' + str(player.hp) + pbar + \
              c.res + separ + c.red + c.inv +\
              c.bolt + 'HP:' + str(enemy.hp) + ebar + c.res
    return(bar)


def mp_bar():
    from classes import Colors as c
    pmp = player.mp
    emp = enemy.mp

    psection = (player.mp_max / 30)
    esection = (enemy.lvl*30 / 30)
    pbar = str( ' ' * int( pmp/psection-len(str(player.mp) ) + 4 ) )
    ebar = str( ' ' * int( emp/esection-len(str(enemy.mp) ) + 4 ) )
    separ = (' ' * ( 48 - len(pbar) - len( str(player.mp) ) ) )
    bar = c.blue + c.inv + c.bolt + 'MP:' + str(player.mp) + pbar + c.res  +\
          separ + c.blue + c.bolt + c.inv + 'MP:' + str(enemy.mp) + ebar + c.res
    return(bar)


def xp_bar():
    from classes import Colors as c
    pmp = player.exp
    section = math.floor(player.exp_to_lvl/19)
    pbar = str( ' ' * int(pmp/section) )
    mbar = str( ' ' * (47 - len(pbar) - len(' из ') - \
           len(str(player.exp_to_lvl)) - len(str(player.exp))))
    bar = c.light_blue + c.inv + c.bolt + 'EXP:' + str(player.exp) +\
          ' из ' + str(player.exp_to_lvl) + pbar + c.res + mbar +\
          c.light_blue + c.inv + 'EXP:' + str(enemy.exp) + '     ' + c.res
    return(bar)

