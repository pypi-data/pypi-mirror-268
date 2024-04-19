import requests

class NewsAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2/"

    def get_top_headlines(self, country='us', category=None, language=None):
        params = {
            'apiKey': self.api_key,
            'country': country
        }
        if category:
            params['category'] = category
        if language:
            params['language'] = language

        response = requests.get(self.base_url + 'top-headlines', params=params)
        response.raise_for_status()  # Raise an error for non-200 status codes

        return response.json()['articles']
