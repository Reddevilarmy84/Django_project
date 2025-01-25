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

#year = 2020
#pages = 9
#url = f'https://13.lordfilm-dc.com/films-{year}/page/{page}'

def pars_lord_film(year, pages):
    new_list = []
    id = 0
    for page in range(1, pages + 1):
        url = f'https://13.lordfilm-dc.com/films-{year}/page/{page}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml') #html.parser по умолчанию
        th_item = soup.find_all('a', class_="th-in with-mask")
        for item in th_item:
            new_dict = {}
            new_dict['id'] = id
            new_dict['name'] = item.find('div', class_="th-title").get_text()
            new_dict['link'] = item.get('href')
            new_dict['img'] = 'https://13.lordfilm-dc.com/' + item.find('img').get('src')
            new_dict['year'] = year
            new_list.append(new_dict)
            id += 1
    return new_list
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


#new_list = pars_lord_film(year, pages)        #спарсили url
#dict_to_json(new_list, path_to_json)        #записали список словарей в виде JSON
#dict_from_json = json_to_dict(path_to_json)         #записали в переменную список словарей, созданный из JSON


#for item in dict_from_json:
#    print(item)








