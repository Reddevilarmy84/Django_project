import os
from utils import dict_to_json, json_to_dict, pars_lord_film

#print(soup.prettify())

# Получаем путь к директории текущего скрипта
this_py_dir = os.path.dirname(os.path.abspath(__file__))

# Переходим на уровень выше
parent_dir = os.path.dirname(this_py_dir)

# Получаем путь к JSON
path_to_json = os.path.join(this_py_dir, 'films.json')


year = 2023
page = 3
url = f'https://13.lordfilm-dc.com/films-{year}/page/{page}'


new_list = pars_lord_film(year, url)

dict_to_json(new_list, path_to_json) #записали список словарей в виде JSON

dict_from_json = json_to_dict(path_to_json) #записали в переменную список словарей, созданный из JSON

for item in dict_from_json:
    print(item)








