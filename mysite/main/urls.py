from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('abouts', views.abouts, name='abouts'),
    path('contact', views.contact, name='contact'),
    path('java_script', views.java_script, name='java-script'),
    path('trading_view', views.trading_view, name='trading_view'),
    path('trading_view/<str:urrl>', views.trading_view, name='trading_view'),
]

