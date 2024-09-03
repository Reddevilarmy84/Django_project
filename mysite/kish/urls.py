from django.urls import path
from . import views

urlpatterns = [
    path('', views.kish, name='kish'),
    path('about_kish', views.about_kish, name='about_kish'),
]
