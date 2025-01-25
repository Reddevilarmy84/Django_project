from . import views
from django.urls import path

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('<int:pk>/update', views.BlogUpdateView.as_view(), name='blog_update'),
    path('<int:pk>/delete', views.BlogDeleteView.as_view(), name='blog_delete'),
]