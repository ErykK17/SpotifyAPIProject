from django.urls import path
from .views import MYSpotifyTopLists, HomeView, RequestUserAuth

app_name = 'api'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('toplists/', MYSpotifyTopLists.as_view(), name='toplists'),
    path('request-auth/', RequestUserAuth.as_view(), name='request-auth'),
]