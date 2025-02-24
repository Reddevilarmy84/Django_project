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


def pars_lord_film(year:int, start_page:int = 1, end_page:int = None):
    if end_page is None:
        end_page = 1
    new_list = []
    for page in range(start_page, int(end_page) + 1):
        url = f'https://13.lordfilm-dc.com/films-{year}/page/{page}'
        try:
            response = requests.get(url)
            print(f'Парсим: {url}')
        except:
            print(f'Disconect: {url}')
            new_dict = {}
            new_dict['year'] = year
            new_dict['page'] = page
            new_dict['name'] = None
            new_dict['link'] = None
            new_dict['img'] = None
            new_list.append(new_dict)
        else:
            soup = BeautifulSoup(response.text, 'lxml') #html.parser по умолчанию
            th_item = soup.find_all('a', class_="th-in with-mask")
            for item in th_item:
                new_dict = {}
                new_dict['year'] = year
                new_dict['page'] = page
                new_dict['name'] = item.find('div', class_="th-title").get_text()
                new_dict['link'] = item.get('href')
                new_dict['img'] = 'https://13.lordfilm-dc.com/' + item.find('img').get('src')
                new_list.append(new_dict)
    return new_list


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

