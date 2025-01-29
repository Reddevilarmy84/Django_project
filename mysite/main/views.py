from django.shortcuts import render
from .parser import pars_lord_film, dict_to_json, json_to_dict, pars_trading_view, url_trading_view, path_to_json_stocks, path_to_json, path_to_json_data
import os
from typing import Optional


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


def trading_view(request, urrl = 'market-movers-all-stocks'):
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


def parser(request, year: Optional[int] = None, pages: Optional[int] = None):
    print(f'\nстарт\n')
    json_data = json_to_dict(path_to_json)
    print(f'прочитали список словарей из старого JSON\n')
    #---------------------------------------------------------------------------------
    if not json_data:
        print('if not json_data: информации в JSON нет ')
        new_list = pars_lord_film(year=2020, pages=3)
        print('if not json_data: спарсили сайт. По умолчанию выставлено year=2020, pages=3 ')
        dict_to_json(new_list, path_to_json)
        print('if not json_data: запаковали JSON ')
        json_data = json_to_dict(path_to_json)
        print('if not json_data: распаковали JSON')
    #---------------------------------------------------------------------------------
    else:#если есть информации
        print(f'Год:{json_data[-1]['year']} страниц:{json_data[-1]['page']} в Json')                     #
##---------------------------------------------------------------------------------
    print(f'Принимаем параметры запроса')
    year = request.GET.get('year', year)
    pages = request.GET.get('pages', pages)
    print(f'Год:{year} Страниц:{pages}')
##---------------------------------------------------------------------------------
    if year is None or not year:
        year = int(json_data[-1]['year'])
        print(f'if year is None or not year: установили Год:{year}')
        if pages is None or not pages:
            pages = int(json_data[-1]['page'])
            print(f'if year is None or not year: установили Страниц:{pages}')
##---------------------------------------------------------------------------------
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

            if int(json_data[-1]['page']) >= int(pages):
                print(f'Спарсено больше страниц, чем запрошено:')
                print('Не парсим')
                # пересоздаем список согласно запросу страниц и в data выводим
                json_data = [i for i in json_data if int(i['page']) <= int(pages) ]
                print(f'Пересоздаем список согласно запросу страниц и выводим в Data')
            else:       # если запрос на большее колличество страниц, а такого количества нет в JSON

                print('ФИЛЬМОВ МЕНЬШЕ, ЧЕМ ТЫ ХОЧЕШЬ!')

                new_list = pars_lord_film(year, pages)
                print(f'Парсим Год:{year} страниц:{pages}')
                print(f'Запаковываем в JSON')
                dict_to_json(new_list, path_to_json)
                print(f'Распаковываем из JSON')
                json_data = json_to_dict(path_to_json)
    print(f'\nфиниш\n')

    data = {
        'title': 'MadJunior: parser',
        'header': 'Парсинг сайта LordFilms',
        'JsonData': json_data,
        'year': year,
        'pages': pages,
    }

    return render(request, 'main/parser.html', data)
