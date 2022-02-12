from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from django.views.generic import DetailView, ListView

from .models import Favorite

def remove_from_watchlist(request):
    name = request.GET['name']
    if name:
        thing = Favorite.objects.get(name=name)
        thing.delete()
    cryptos = Favorite.objects.all()
    context = {
        'cryptos': cryptos
    }
    return render(request, 'cryptos/index.html', context)

def add_favorite(request):
    ticker = request.POST['ticker']
    name = request.POST['name']
    if ticker and name:
        new_fav = Favorite(name=name, ticker=ticker)
        new_fav.save()

    cryptos = Favorite.objects.all()
    context = {
        'cryptos': cryptos
    }
    return render(request, 'cryptos/index.html', context)

class IndexView(ListView):
    template_name = 'cryptos/index.html'
    context_object_name = 'cryptos'

    def get_queryset(self):
        return Favorite.objects.all()

class DetailView(DetailView):
    template_name = 'cryptos/detail.html'
    context_object_name = 'crypto'

    def get_object(self):
        thing = get_object_or_404(Favorite, ticker__exact=self.kwargs['ticker'])
        return thing


