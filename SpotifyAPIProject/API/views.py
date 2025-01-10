from django.shortcuts import render
from django.views.generic import ListView, TemplateView, RedirectView
from django.shortcuts import redirect
from dotenv import load_dotenv
import os
from django.urls import reverse
from urllib.parse import urlencode


class HomeView(TemplateView):
    template_name = 'home.html'

class MYSpotifyTopLists(TemplateView):
    template_name = 'toplists.html'

class RequestUserAuth(RedirectView):
    spotify_url = 'https://accounts.spotify.com/authorize'

    load_dotenv()
    client_id = os.getenv('CLIENTID')

    def get_redirect_url(self, *args, **kwargs):
        uri = self.request.build_absolute_uri(reverse('api:toplists'))
        print(uri)
        query_params = {
            'client_id': self.client_id,
            'response_type': 'code',
            'scope': 'user-top-read',
            'redirect_uri': self.request.build_absolute_uri(reverse('api:toplists')),
        }

        query_string = '&'.join([f'{key}={value}' for key, value in query_params.items()])
        auth_url = f'{self.spotify_url}?{query_string}'
        print(auth_url)
        return auth_url
    def get(self, request, *args, **kwargs):
        return redirect(self.get_redirect_url(*args, **kwargs))