from django.shortcuts import render


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
        'header': 'Ссылки на Вспомагательные материалы',
    }
    return render(request, 'main/contacts.html', data)

def java_script(request):
    data = {
        'title': 'MadJunior: JavaScript',
        'header': 'Практикуем JavaScript',
    }
    return render(request, 'main/JavaScript.html', data)
