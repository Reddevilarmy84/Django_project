from django.shortcuts import render
from .parser_trading_views import pars_trading_view


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
    new_list = pars_trading_view(f'https://ru.tradingview.com/markets/stocks-russia/{urrl}')
    data = {
        'title': 'MadJunior: Акции',
        'header': 'Акции',
        'json_data_stocks': new_list
    }
    return render(request, 'main/trading_view.html', data)


