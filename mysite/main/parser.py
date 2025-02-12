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


def pars_trading_view(url):
    new_list = []
    id = 0
    response = requests.get(url)
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
#______________________боремся с позитивом___________________________________________________________________________
        try:
            new_dict['cell_fall'] = item.find('span', class_="negative-p_QIAEOQ").text
        except:
            new_dict['cell_fall'] = 'None'
        try:
            new_dict['cell_raise'] = item.find('span', class_="positive-p_QIAEOQ").text
        except:
            new_dict['cell_raise'] = 'None'

# ______________________боремся с позитивом__________________________________________________________________________
#        new_dict['название'] = item.find('sup', class_ ="apply-common-tooltip tickerDescription-GrtoTeat").text

        #группа
        try:
            new_dict['group'] = item.find('a', class_="link-KcaOqbQP apply-common-tooltip").text
        except:
            new_dict['group'] = 'None'
        new_list.append(new_dict)
        id += 1
    return new_list

def pars_lord_film(year, pages):
    if not pages:
        pages = 1
    new_list = []
    page_id = 1
    for page in range(1, int(pages) + 1):
        url = f'https://13.lordfilm-dc.com/films-{year}/page/{page}'
        try:
            response = requests.get(url)
        except:
            print(f'Disconect: {url}')
            new_dict = {}
            new_dict['page'] = page_id
            new_dict['name'] = f'Страница {page} не спарсилась'
            new_dict['link'] = None
            new_dict['img'] = None
            new_dict['year'] = int(year)
            new_list.append(new_dict)
        else:
            soup = BeautifulSoup(response.text, 'lxml') #html.parser по умолчанию
            th_item = soup.find_all('a', class_="th-in with-mask")
            for item in th_item:
                new_dict = {}
                new_dict['page'] = page_id
                new_dict['name'] = item.find('div', class_="th-title").get_text()
                new_dict['link'] = item.get('href')
                new_dict['img'] = 'https://13.lordfilm-dc.com/' + item.find('img').get('src')
                new_dict['year'] = int(year)
                new_list.append(new_dict)
        page_id += 1
    return new_list


def parser():
    url = 'https://lenta.ru/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    print(soup.prettify())
    items = soup.find_all('img')
    Lst = []
    Dict = {}

    for i in items:
        Lst.append(i)

    return Lst


def dict_to_json(dict_list, filename):
    try:
        json_str = json.dumps(dict_list, ensure_ascii=False)
        with open(filename, "w", encoding="utf-8") as file:
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
        print(f"Ошибка при чтении JSON из файла или преобразовании в список словарей: {e}")
        return None



#news = parser()

#for i in news:
#    print(i)