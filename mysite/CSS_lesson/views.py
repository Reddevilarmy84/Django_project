from django.shortcuts import render

# Create your views here.
def CSS_lesson(request):
    return render(request, 'CSS_lesson/CSS_lesson.html')