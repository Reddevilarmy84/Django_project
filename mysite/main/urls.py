from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('abouts', views.abouts, name='abouts'),
    path('contact', views.contact, name='contact'),
    path('java_script', views.java_script, name='java-script'),
    path('parser', views.parser, name='parser'),
]
