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


def parser(request, year: Optional[int] = None, pages: Optional[int] = None, last_seach: Optional[int] = None):
    last_seach = request.GET.get('last_seach', last_seach)
    json_data = json_to_dict(path_to_json)
    print(f'Список фильмов в Json:')

    for item in json_data:
        print(f'                  {item['name']}')

    if not json_data:
        new_list = pars_lord_film(year=2025, pages=1)
        dict_to_json(new_list, path_to_json)
        json_data = json_to_dict(path_to_json)
    else:
        if last_seach is not None:
            year = request.GET.get('year', year)
            pages = request.GET.get('pages', pages)
            json_data = json_to_dict(path_to_json)
            if year != json_data[0]['year']:
                if year is not None:
                    if pages is None:
                        pages = 1
                    new_list = pars_lord_film(year, pages)
                    print('парсим')
                    dict_to_json(new_list, path_to_json)
                    json_data = json_to_dict(path_to_json)
                else:
                    year = None
                    json_data = None
            else:
                if json_data[-1]['page'] >= int(pages):
                    print('не парсим')
                    json_data = [i for i in json_data if int(i['page']) <= int(pages) ]
                else:
                    print('ФИЛЬМОВ МЕНЬШЕ, ЧЕМ ТЫ ХОЧЕШЬ')
                    new_list = pars_lord_film(year, pages)
                    print('парсим')
                    dict_to_json(new_list, path_to_json)
                    json_data = json_to_dict(path_to_json)
        else:
            json_data = json_to_dict(path_to_json)
            year = None
    data = {
        'title': 'MadJunior: parser',
        'header': 'Парсинг сайта LordFilms',
        'JsonData': json_data,
        'year': year,
        'pages': pages,
    }

    return render(request, 'main/parser.html', data)
