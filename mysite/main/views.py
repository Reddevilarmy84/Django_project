from django.shortcuts import render
from .parser import pars_lord_film, dict_to_json, json_to_dict, pars_trading_view, url_trading_view, \
    path_to_json_stocks, path_to_json, Colors
from random import randint


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


def trading_view(request, urrl='market-movers-all-stocks'):
    url_trading_view = f'https://ru.tradingview.com/markets/stocks-russia/{urrl}'
    #   path_to_json_stocks = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'stocks.json')
    new_list = pars_trading_view(url_trading_view)
    dict_to_json(new_list, path_to_json_stocks)
    #    json_data_stocks = json_to_dict(path_to_json_stocks)
    data = {
        'title': 'MadJunior: Акции',
        'header': 'Акции',
        'json_data_stocks': new_list
    }
    return render(request, 'main/trading_view.html', data)


'''
def parser(request, year: int = None, pages: int = None):
    print(f'\nстарт\n')
    json_data = json_to_dict(path_to_json)
    print(f'прочитали список словарей из старого JSON\n')
    #---------------------------------------------------------------------------------
    if not json_data:
        year = 2020 # если нет фильмов в файле установлено по умолчанию
        pages = 3 # если нет фильмов в файле установлено по умолчанию
        print('if not json_data: информации в JSON нет ')
        new_list = pars_lord_film(year, pages)
        print('if not json_data: спарсили сайт. По умолчанию выставлено year=2020, pages=3 ')
        dict_to_json(new_list, path_to_json)
        print('if not json_data: запаковали JSON ')
        json_data = json_to_dict(path_to_json)
        print('if not json_data: распаковали JSON')
    #---------------------------------------------------------------------------------
    else:#если есть информации
        print(f'Год:{json_data[-1]['year']} страниц:{json_data[-1]['page']} в Json')
#---------------------------------------------------------------------------------
    print(f'Принимаем параметры запроса')
    year = request.GET.get('year', year)
    pages = request.GET.get('pages', pages)
    print(f'Год:{year} Страниц:{pages}')
#---------------------------------------------------------------------------------
    if year is None or not year:
        year = int(json_data[-1]['year'])
        print(f'if year is None or not year: установили Год:{year}')
        if pages is None or not pages:
            pages = int(json_data[-1]['page'])
            print(f'if year is None or not year: установили Страниц:{pages}')
#---------------------------------------------------------------------------------
    else:
        print(f'Год в запросе:{year}')
        if pages is None:
            pages = 1
            print(f'if pages is None: установили страниц:{pages}')
        ##--------------------------------------------------------------------------------------------------
        if int(year) != int(json_data[0]['year']):
            print(f'Год не совпадает с годом в файле. Год:{year}')
            new_list = pars_lord_film(year, pages)
            print('Парсим год:{year} страниц:{pages}')
            dict_to_json(new_list, path_to_json)
            print('Запаковываем в JSON')
            json_data = json_to_dict(path_to_json)
            print('Распаковываем из JSON')
        ##--------------------------------------------------------------------------------------------------
        else:  # если год равен году в файле
            # проверяем сколько станиц в файле
            if not pages or pages is None:
                pages = json_data[-1]['page']
                print(f'if not pages or pages is None: Установили согласно JSON на = {pages}')
            ##--------------------------------------------------------------------------------------------------
            if int(json_data[-1]['page']) >= int(pages):
                print(f'Спарсено больше страниц, чем запрошено:')
                print('Не парсим')
                # пересоздаем список согласно запросу страниц и в data выводим
                json_data = [i for i in json_data if int(i['page']) <= int(pages) ]
                print(f'Пересоздаем список согласно запросу страниц и выводим в Data')
            else:       # если запрос на большее колличество страниц, а такого количества нет в JSON
                ##--------------------------------------------------------------------------------------------------

                print('ФИЛЬМОВ МЕНЬШЕ, ЧЕМ ТЫ ХОЧЕШЬ!')
                ##--------------------------------------------------------------------------------------------------
                new_list = pars_lord_film(year, pages)
                print(f'Парсим Год:{year} страниц:{pages}')
                print(f'Запаковываем в JSON')
                dict_to_json(new_list, path_to_json)
                print(f'Распаковываем из JSON')
                json_data = json_to_dict(path_to_json)
    for i in json_data:
        if not i['link'] and not i['img']:
            new_new_list = pars_lord_film(i["year"], i["page"], i["page"])
            print(f'Репарсинг {i["page"]}\n')
            index = json_data.index(i)
            del json_data[index]
            new_new_list.reverse()
            for i in new_new_list:
                json_data.insert(index, i)
            dict_to_json(json_data, path_to_json)

    print(f'\nфиниш\n')
    ##--------------------------------------------------------------------------------------------------
    data = {
        'title': 'MadJunior: parser',
        'header': 'Парсинг сайта LordFilms',
        'JsonData': json_data,
        'year': year,
        'pages': pages,
    }
    ##--------------------------------------------------------------------------------------------------
    return render(request, 'main/parser.html', data)'''


def parser(request, year: int = None, pages: int = None):
    #создать список для контекста
    json_data = []
    #вернули список фильмов из БД
    json_data_db = json_to_dict(path_to_json)
    #генерируем список случайных фильмов, исключая дубликаты
    if json_data_db:
        for i in range(0, 6):
            film = json_data_db[randint(0, len(json_data_db) - 1)]
            if film in json_data:
                pass
            else:
                json_data.append(film)
    content = 'случайные фильмы из базы'
    #принимаем параметры запроса
    year = request.GET.get('year', year)
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
    # отображение хода работы скрипта в консоли
    #print(f"{Colors.green}year='{year}'{type(year)}{Colors.reset}")
    #print(f"{Colors.green}pages='{pages}'{type(pages)}{Colors.reset}\n")
    if year is not None:
        #отображение хода работы скрипта в консоли
        #print(f"{Colors.green}json_data_db={Colors.reset}")
        #for i in json_data_db:
            #print(f"{Colors.green}год:{i['year']} стр:{i['page']} название:{i['name']}'{Colors.reset}")
        if json_data_db:
            json_data = [i for i in json_data_db if i['year'] == year and i['page'] <= pages]

        if json_data:
            if json_data[-1]['page'] < pages:
                print(f"страниц меньше чем просили")
                json_data_new = pars_lord_film(year, json_data[-1]['page'] + 1, pages)
                content = 'Спарсили'
                # отображение хода работы скрипта в консоли
                #print(f"\njson_data_new:")
                #for i in json_data_new:
                #    print(i['year'], i['page'], i['name'])
                json_data.extend(json_data_new)
                json_data_db.extend(json_data_new)
                json_data_db.sort(key=lambda x: (x['year'], x['page']))
                # отображение хода работы скрипта в консоли
                #print(f"\njson_data_db:")
                #for i in json_data_db:
                #    print(i['year'], i['page'], i['name'])
                dict_to_json(json_data_db, path_to_json)
            else:
                print(f'\nне парсим. взяли из DB')
                content = 'Не парсим. Взяли из базы данных'

        else:
            print(f"в json_data нет ничего")
            json_data = pars_lord_film(year, 1, pages)
            json_data_db.extend(json_data)
            json_data_db.sort(key=lambda x: (x['year'], x['page']))
            dict_to_json(json_data_db, path_to_json)
            content = 'Спарсили'
        # отображение хода работы скрипта в консоли
        #print(f'{Colors.green}\njson_data:{Colors.reset}')
       # for i in json_data:
        #    print(f"{Colors.green}json_data={i['year']} {i['page']} {i['name']}{Colors.reset}")
        #print(f'{Colors.green}\njson_data_db:{Colors.reset}')
        #for i in json_data_db:
        #    print(f"{Colors.green}json_data_db={i['year']} {i['page']} {i['name']}{Colors.reset}")

    context = {
        'title': 'MadJunior: parser',
        'header': 'Парсинг сайта LordFilms',
        'JsonData': json_data,
        'year': year,
        'pages': pages,
        'content': content,
    }
    return render(request, 'main/parser.html', context)
