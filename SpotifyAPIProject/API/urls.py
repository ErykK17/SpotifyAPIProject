from django.urls import path

from .views import HomeView, RequestUserAuth, TopSongs, TopArtists

app_name = 'api'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('request-auth/', RequestUserAuth.as_view(), name='request-auth'),
    path('top-songs/', TopSongs.as_view(), name='top-songs'),
    path('top-artists/', TopArtists.as_view(), name='top-artists')
]