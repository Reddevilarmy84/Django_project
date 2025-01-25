from . import views
from django.urls import path

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('create', views.create, name='create'),
]