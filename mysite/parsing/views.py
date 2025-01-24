from django.shortcuts import render
from .models import Articles

# Create your views here.
def home_p(request):
    news = Articles.objects.all()
    return render(request, 'parsing/home_p.html', {'news': news})