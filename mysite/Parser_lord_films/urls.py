from django.urls import path
from . import views

urlpatterns = [
    path('', views.Parser_lord_films, name='Parser_lord_films'),
    path("<int:year>", views.Parser_lord_films),
    path("<int:year>/<int:pages>", views.Parser_lord_films),
]
