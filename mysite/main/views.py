from django.shortcuts import render
import os
import json

# Получаем путь к директории текущего скрипта
this_py_dir = os.path.dirname(os.path.abspath(__file__))

# Переходим на уровень выше
parent_dir = os.path.dirname(this_py_dir)

pre_parent_dir = os.path.dirname(parent_dir)

# Получаем путь к JSON
path_to_json = os.path.join(pre_parent_dir, 'Python', 'parser', 'films.json')



def json_to_dict(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            json_str = file.read()
            dict_list = json.loads(json_str)
        return dict_list
    except (TypeError, ValueError, IOError) as e:
        print(f"Ошибка при чтении JSON из файла или преобразовании в список словарей: {e}")
        return None


def index(request):
    data = {
        'title': 'MadJunior: Главная!',
        'header': 'MadJunior',
    }
    return render(request, 'main/index.html', data)


def abouts(request):
    data = {
        'title': 'MadJunior: Про нас',
        'header': 'Про нас',
    }
    return render(request, 'main/about.html', data)


def contact(request):
    data = {
        'title': 'MadJunior: Вспомагательные материалы',
        'header': 'Вспомагательные материалы',
    }
    return render(request, 'main/contacts.html', data)

def java_script(request):
    data = {
        'title': 'MadJunior: JavaScript',
        'header': 'Практикуем JavaScript',
    }
    return render(request, 'main/JavaScript.html', data)


def parser(request):
    json_data = json_to_dict(path_to_json)
    data = {
        'title': 'MadJunior: parser',
        'header': 'Парсинг сайта LordFilms',
        'JsonData': json_data,
    }

    return render(request, 'main/parser.html', data)