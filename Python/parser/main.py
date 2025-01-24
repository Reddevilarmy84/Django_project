import requests
from bs4 import BeautifulSoup
import json
import os
import time

#print(soup.prettify())

# Получаем путь к директории текущего скрипта
script_dir = os.path.dirname(os.path.abspath(__file__))

# Переходим на уровень выше
parent_dir = os.path.dirname(script_dir)

# Получаем путь к JSON
path_to_json = os.path.join(script_dir, 'films.json')

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

        return dict_list, print(dict_list)
    except (TypeError, ValueError, IOError) as e:
        print(f"Ошибка при чтении JSON из файла или преобразовании в список словарей: {e}")
        return None


year = 2023
page = 3
url = f'https://13.lordfilm-dc.com/films-{year}/page/{page}'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml') #html.parser по умолчанию

th_item = soup.find_all('a', class_="th-in with-mask")

list = []
id = 0

for item in th_item:
    dict_1 = {}
    dict_1['id'] = id
    dict_1['name'] = item.find('div', class_="th-title").get_text()
    dict_1['link'] = item.get('href')
    dict_1['img'] = 'https://13.lordfilm-dc.com/' + item.find('img').get('src')
    dict_1['year'] = year
    list.append(dict_1)
    id += 1

print(f'список:')

for item in list:

    print(f'{item}')

print(f'конец списка')

dict_to_json(list, path_to_json)

json_to_dict(path_to_json)
print(dict_list)







