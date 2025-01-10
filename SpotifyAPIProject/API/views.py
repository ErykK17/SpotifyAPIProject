from django.shortcuts import render
from django.views.generic import ListView, TemplateView

class HomePage(TemplateView):
    template_name = 'home.html'


class MYSpotifyTopLists(ListView):
    template_name = 'toplists.html'
    context_object_name = 'topItem'