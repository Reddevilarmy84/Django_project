from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dungeon_master, name='Dungeon_master'),
]
