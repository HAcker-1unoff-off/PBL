from django.shortcuts import render
from django.conf import settings 
from django.http import JsonResponse
import requests
from django.core.paginator import Paginator

def index(request):
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey=dd3f941637104e51b395ebd7b7814b22'
    response = requests.get(url)
    data = response.json()
    articles = data.get('articles', [])
    return render(request, 'newsapp/index.html', {'articles': articles})

def fetch_news(request):
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey=dd3f941637104e51b395ebd7b7814b22'
    '''params = {
        #'country': 'us',
       # 'apiKey': 'dd3f941637104e51b395ebd7b7814b22',
    #}'''
    response = requests.get(url, '''params=params''')
    data = response.json()
    print("API response:", data)

    articles = data.get('articles', [])
    return JsonResponse({'articles': articles})

'''def index(request):
    api_key = settings.NEWS_DATA_API_KEY

    url = "https://newsdata.io/api/1/news"
    params = {
        "apikey": api_key,
        "country": "in",
        "language": "en",
        "category": "top"
    }
    response = requests.get(url, params=params)
    data = response.json()

    if data.get("status") == "success":
        articles  = data.get("results", [])
    else: 
        articles = []

    return render(request, "newsapp/index.html", {"articles": articles})'''

'''def news_home(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', 'general')
    page_number = request.GET.get('page', 1)

    url = f'https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={settings.NEWS_API_KEY}'
    if query:
        url = f'https://newsapi.org/v2/everything?q={query}&apiKey={settings.NEWS_API_KEY}'

    response = requests.get(url)
    data = response.json()
    articles = data.get('articles', [])

    paginator = Paginator(articles, 6)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': query,
        'category': category,
    }

    return render(request, 'newsapp/index.html', context)'''