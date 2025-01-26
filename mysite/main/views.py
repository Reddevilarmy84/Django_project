from django.shortcuts import render
from .parser import pars_lord_film, dict_to_json, json_to_dict, pars_trading_view, url_trading_view, path_to_json_stocks
import os


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


def trading_view(request):
    url_trading_view = 'https://ru.tradingview.com/markets/stocks-russia/market-movers-all-stocks/'
    path_to_json_stocks = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'stocks.json')
    new_list = pars_trading_view(url_trading_view)
    dict_to_json(new_list, path_to_json_stocks)
    json_data_stocks = json_to_dict(path_to_json_stocks)
    data = {
        'title': 'MadJunior: Акции',
        'header': 'Акции',
        'json_data_stocks': new_list
    }
    return render(request, 'main/trading_view.html', data)


def parser(request, year=2025, pages=1):
    path_to_json = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'films.json')
    year = request.GET.get('year', year)
    pages = int(request.GET.get('pages', pages))
    new_list = pars_lord_film(year, pages)
    dict_to_json(new_list, path_to_json)
    json_data = json_to_dict(path_to_json)
    data = {
        'title': 'MadJunior: parser',
        'header': 'Парсинг сайта LordFilms',
        'JsonData': json_data,
        'year': year,
        'pages': pages,
    }
    return render(request, 'main/parser.html', data)
