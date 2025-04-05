import requests
from bs4 import BeautifulSoup


url_trading_view = 'https://ru.tradingview.com/markets/stocks-russia/market-movers-all-stocks/'


def pars_trading_view(url):
    new_list = []
    id = 0
    try:
        response = requests.get(url)
    except:
        print('disconect')
    else:
        soup = BeautifulSoup(response.text, 'lxml')
        find = soup.find_all('tr', class_="row-RdUXZpkv listRow")
        for item in find:
            new_dict = {}
            new_dict['id'] = id
            new_dict['title'] = item.find('a').get('title')
            #изображение
            try:
                new_dict['img'] = item.find('img').get('src')
            except: new_dict['img'] = 'None'
            #цена
            try:
                new_dict['cell'] = item.find('td', class_="cell-RLhfr_y4 right-RLhfr_y4").text
            except: new_dict['cell'] = 'None'
            try:
                new_dict['cell_fall'] = item.find('span', class_="negative-p_QIAEOQ").text
            except:
                new_dict['cell_fall'] = 'None'
            try:
                new_dict['cell_raise'] = item.find('span', class_="positive-p_QIAEOQ").text
            except:
                new_dict['cell_raise'] = 'None'
            #группа
            try:
                new_dict['group'] = item.find('a', class_="link-KcaOqbQP apply-common-tooltip").text
            except:
                new_dict['group'] = 'None'
            new_list.append(new_dict)
            id += 1
    return new_list