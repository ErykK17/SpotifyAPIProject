from django.urls import path

from .views import HomeView, MYSpotifyTopLists, RequestUserAuth, TopSongs, TopArtists

app_name = 'api'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('toplists/', MYSpotifyTopLists.as_view(), name='toplists'),
    path('request-auth/', RequestUserAuth.as_view(), name='request-auth'),
    path('top-songs/', TopSongs.as_view(), name='top-songs'),
    path('top-artists/', TopArtists.as_view(), name='top-artists')
]