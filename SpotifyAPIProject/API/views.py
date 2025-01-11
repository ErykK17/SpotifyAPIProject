import os

from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, RedirectView, TemplateView
from dotenv import load_dotenv

from .utils import get_access_token, get_top_items


class HomeView(TemplateView):
    template_name = 'home.html'


class RequestUserAuth(RedirectView):
    spotify_url = 'https://accounts.spotify.com/authorize'

    load_dotenv()
    client_id = os.getenv('CLIENTID')

    def get_redirect_url(self, *args, **kwargs):
        uri = self.request.build_absolute_uri(reverse('api:toplists'))
        query_params = {
            'client_id': self.client_id,
            'response_type': 'code',
            'scope': 'user-top-read',
            'redirect_uri': self.request.build_absolute_uri(reverse('api:toplists')),
        }

        query_string = '&'.join([f'{key}={value}' for key, value in query_params.items()])
        auth_url = f'{self.spotify_url}?{query_string}'
        return auth_url
    def get(self, request, *args, **kwargs):
        return redirect(self.get_redirect_url(*args, **kwargs))

class MYSpotifyTopLists(TemplateView):
    template_name = 'toplists.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        error = self.request.GET.get('error', None)
        if error:
            context['error'] = error
            return context
        code = self.request.GET.get('code', None)
        redirect_uri = self.request.build_absolute_uri(reverse('api:toplists'))
        access_token = get_access_token(code, redirect_uri)
        context['access_token'] = access_token
        return context
    

class TopSongs(TemplateView):
    template_name = 'topsongs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        access_token = self.request.GET.get('access_token')
        songs = get_top_items('tracks', access_token, time_range='short_term')
        context['songs'] = songs
        return context

class TopArtists(TemplateView):
    template_name = 'topartists.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        access_token = self.request.GET.get('access_token')
        artists = get_top_items('artists', access_token, time_range='short_term')
        context['artists'] = artists
        return context