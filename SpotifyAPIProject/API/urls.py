from django.urls import path
from .views import MYSpotifyTopLists

urlpatterns = [
    path('toplists/', MYSpotifyTopLists.as_view(), name='toplists'),
]