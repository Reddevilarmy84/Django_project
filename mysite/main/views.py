from django.shortcuts import render
from .parser import pars_lord_film, dict_to_json, json_to_dict, path_to_json


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
    year = 2022
    pages = 1
    new_list = pars_lord_film(year, pages) #спарсили
    dict_to_json(new_list, path_to_json) #заJSONили
    json_data = json_to_dict(path_to_json) #разJSONили в переменную
    data = {
        'title': 'MadJunior: parser',
        'header': 'Парсинг сайта LordFilms',
        'JsonData': json_data,
        'year': year,
        'pages': pages,
    }
    return render(request, 'main/parser.html', data)
