








from django.urls import path
from . import views
from django.urls import path, include



urlpatterns = [
    path('', views.index, name='home'),
    path('abouts', views.abouts, name='abouts'),
    path('contact', views.contact, name='contact'),
    path('blocks', views.blocks, name='blocks'),
]
