import os
import requests
from bs4 import BeautifulSoup
import json

# Получаем путь к директории текущего скрипта
this_py_dir = os.path.dirname(os.path.abspath(__file__))
# Переходим на уровень выше
parent_dir = os.path.dirname(this_py_dir)
# Получаем путь к JSON
path_to_json = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'films.json')
path_to_json_stocks = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'stocks.json')
url_trading_view = 'https://ru.tradingview.com/markets/stocks-russia/market-movers-all-stocks/'


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


def pars_trading_view(url):
    new_list = []
    id = 0
    try:
        response = requests.get(url)
    except:
        print('disconect')
    else:
        soup = BeautifulSoup(response.text, 'lxml')
        find = soup.find_all('tr', class_="row-RdUXZpkv listRow")
        for item in find:
            new_dict = {}
            new_dict['id'] = id
            new_dict['title'] = item.find('a').get('title')
            #изображение
            try:
                new_dict['img'] = item.find('img').get('src')
            except: new_dict['img'] = 'None'
            #цена
            try:
                new_dict['cell'] = item.find('td', class_="cell-RLhfr_y4 right-RLhfr_y4").text
            except: new_dict['cell'] = 'None'
            try:
                new_dict['cell_fall'] = item.find('span', class_="negative-p_QIAEOQ").text
            except:
                new_dict['cell_fall'] = 'None'
            try:
                new_dict['cell_raise'] = item.find('span', class_="positive-p_QIAEOQ").text
            except:
                new_dict['cell_raise'] = 'None'
            #группа
            try:
                new_dict['group'] = item.find('a', class_="link-KcaOqbQP apply-common-tooltip").text
            except:
                new_dict['group'] = 'None'
            new_list.append(new_dict)
            id += 1
    return new_list




