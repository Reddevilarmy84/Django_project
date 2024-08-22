
from django.urls import path
from . import views

urlpatterns = [
    path('', views.CSS_lesson, name='CSS_lesson'),
    path('playlist', views.playlist, name='playlist'),
    path('four_lessons', views.four_lessons, name='four_lessons'),
]
