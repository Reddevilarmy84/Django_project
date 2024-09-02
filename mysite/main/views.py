from django.shortcuts import render


def index(request):
    data = {

        'title': 'Главная страница',

    }
    return render(request, 'main/index.html', data)


def abouts(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contacts.html')

def blocks(request):
    return render(request, 'main/blocks.html')
