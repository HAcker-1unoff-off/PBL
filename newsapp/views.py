from django.shortcuts import render
from django.conf import settings 
from django.http import JsonResponse
import requests

def index(request):
    return render(request, 'newsapp/index.html')

def fetch_news(request):
    url = f'https://newsapi.org/v2/top-headlines'
    params = {
        'country': 'us',
        'apiKey': 'dd3f941637104e51b395ebd7b7814b22',
    }
    response = requests.get(url, params=params)
    data = response.json()
    print("API response:", data)

    articles = data.get('articles', [])
    return render(request, 'newsapp/index.html', {'articles': articles})