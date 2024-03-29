import requests
from django.shortcuts import render, HttpResponse

from django_base.settings import NEWS_API_KEY

def fetch_news(request):
    response = requests.get(f'https://newsapi.org/v2/everything?q=bitcoin&apiKey={NEWS_API_KEY}')
    if response.status_code != 200:
        return HttpResponse(response.status_code)
    response = response.json()
    return HttpResponse(response['articles'])
