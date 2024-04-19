# news_api/news.py

import requests

class NewsAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_top_headlines(self, country='us'):
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={self.api_key}'
        response = requests.get(url)
        return response.json()

    def search_news(self, query, language='en'):
        url = f'https://newsapi.org/v2/everything?q={query}&language={language}&apiKey={self.api_key}'
        response = requests.get(url)
        return response.json()
