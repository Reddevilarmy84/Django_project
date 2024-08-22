from django.shortcuts import render

# Create your views here.
def CSS_lesson(request):
    return render(request, 'CSS_lesson/CSS_lesson.html')

def playlist(request):
    return render(request, 'CSS_lesson/playlist.html')

def four_lessons(request):
    return render(request, 'CSS_lesson/four_lessons.html')