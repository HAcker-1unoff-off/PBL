from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fetch-news/', views.fetch_news, name='fetch_news'),
]