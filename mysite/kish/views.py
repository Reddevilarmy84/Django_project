from django.shortcuts import render

# Create your views here.
def kish(request):
    return render(request, 'kish/kish.html')

def about_kish(request):
    return render(request, 'kish/about_kish.html')