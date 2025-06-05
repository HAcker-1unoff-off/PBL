from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fetch-news/', views.fetch_news, name='fetch_news'),
    path('polls/', views.poll_list, name='poll_list'),
    path('poll/<int:poll_id>/vote/', views.vote, name='vote'),
    path('poll/<int:poll_id>/results/', views.results, name='results'),
]