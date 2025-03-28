from django.shortcuts import render
from .utils import pars_lord_film, dict_to_json, json_to_dict, path_to_json, Colors
from random import randint

def Parser_lord_films(request, year: int = None, pages: int = None, clear: bool = False):
    font_size = 25
    json_data = []  #создать список для контекста
    clear = request.GET.get('clear', clear)
    if clear:
        dict_to_json(json_data, path_to_json)
        print(f'БД очищена')
    json_data_db = json_to_dict(path_to_json)  #вернули список фильмов из БД
    if json_data_db:  #генерируем список случайных фильмов, исключая дубликаты
        for i in range(0, 6):
            film = json_data_db[randint(0, len(json_data_db) - 1)]
            if film in json_data:
                pass
            else:
                json_data.append(film)
    content = 'случайные фильмы из базы'
    year = request.GET.get('year', year)  #принимаем параметры запроса
    pages = request.GET.get('pages', pages)
    '''проверяем, что year и pages не None, иначе при преобразовании их в int будет TypeError.
    Преобразовать year и pages в int иначе установить значения None.
    year и pages на выходе могут быть либо int, либо None.'''
    if year is not None and pages is not None:
        try:
            year = int(year)
        except ValueError as e:
            print(f"{Colors.red}year не целое число. Установлено None {e}{Colors.reset}")
            year = None
        try:
            pages = int(pages)
        except ValueError as e:
            print(f"{Colors.red}pages не целое число. Установлено None {e}{Colors.reset}")
            pages = None
    '''отображение хода работы скрипта в консоли
    print(f"{Colors.green}year='{year}'{type(year)}{Colors.reset}")
    print(f"{Colors.green}pages='{pages}'{type(pages)}{Colors.reset}\n")'''
    if year is not None:
        '''отображение хода работы скрипта в консоли
        print(f"{Colors.green}json_data_db={Colors.reset}")
        for i in json_data_db:
            print(f"{Colors.green}год:{i['year']} стр:{i['page']} название:{i['name']}'{Colors.reset}")'''
        if json_data_db:
            '''проверяем, есть ли в БД фильмы и генерируем список фильмов по году'''
            json_data = [i for i in json_data_db if i['year'] == year and i['page'] <= pages]
        if json_data:
            '''проверяем наличие информации и совпадение колличества страниц в сгенерированном списке с параметром запроса колличества страниц,
            парсим недостающие страницы, добавляем в список для контекста и в список для БД, сортируем список для БД по году и страницам
            обновляем films.json'''
            if json_data[-1]['page'] < pages:
                print(f"страниц меньше чем просили")
                json_data_new = pars_lord_film(year, json_data[-1]['page'] + 1, pages)
                content = 'Спарсили'
                '''отображение хода работы скрипта в консоли
                print(f"\njson_data_new:")
                for i in json_data_new:
                    print(i['year'], i['page'], i['name'])'''
                json_data.extend(json_data_new)
                json_data_db.extend(json_data_new)
                json_data_db.sort(key=lambda x: (x['year'], x['page']))
                '''отображение хода работы скрипта в консоли
                print(f"\njson_data_db:")
                for i in json_data_db:
                    print(i['year'], i['page'], i['name'])'''
                dict_to_json(json_data_db, path_to_json)
            else:
                print(f'\nне парсим. взяли из DB')
                content = 'Не парсим. Взяли из базы данных'
        else:
            '''проверяем, есть ли в БД фильмы и генерируем список фильмов по году'''
            print(f"в json_data нет ничего")
            json_data = pars_lord_film(year, 1, pages)
            json_data_db.extend(json_data)
            json_data_db.sort(key=lambda x: (x['year'], x['page']))
            dict_to_json(json_data_db, path_to_json)
            content = 'Спарсили'
        '''отображение хода работы скрипта в консоли
        print(f'{Colors.green}\njson_data:{Colors.reset}')
        for i in json_data:
            print(f"{Colors.green}json_data={i['year']} {i['page']} {i['name']}{Colors.reset}")
        print(f'{Colors.green}\njson_data_db:{Colors.reset}')
        for i in json_data_db:
           print(f"{Colors.green}json_data_db={i['year']} {i['page']} {i['name']}{Colors.reset}")'''
    context = {
        'title': 'MadJunior: parser',
        'header': 'Парсинг сайта LordFilms',
        'JsonData': json_data,
        'year': year,
        'pages': pages,
        'content': content,
        'font_size': font_size,
    }
    return render(request, 'main/parser.html', context)

