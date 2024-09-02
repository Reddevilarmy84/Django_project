from django.shortcuts import render

# Create your views here.
def kish(request):
    return render(request, 'kish/kish.html')