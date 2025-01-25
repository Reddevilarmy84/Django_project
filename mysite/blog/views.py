from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Artiсles

def blog_home(request):
    #сортируем данные по дате, можно использовать срез
    blog = Artiсles.objects.order_by('-date')[0:50]
    return render(request, 'blog/blog_home.html', {'blog': blog})

def create(request):
    return render(request, 'blog/create.html')