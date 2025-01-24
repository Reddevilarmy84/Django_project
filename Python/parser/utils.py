import json
import requests
from bs4 import BeautifulSoup



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


def pars_lord_film(year, url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml') #html.parser по умолчанию
    th_item = soup.find_all('a', class_="th-in with-mask")
    new_list = []
    id = 0
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