
from django.urls import path
from . import views




urlpatterns = [
    path('', views.tracks_home, name='tracks'),
    path('add', views.add_note, name='create'),
    path('<int:pk>/', views.TracksDetailView.as_view(), name='detail'),

]