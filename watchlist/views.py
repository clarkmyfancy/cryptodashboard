from django.views.generic import ListView
from django.shortcuts import render

from coinmarketcap_api.api import Api

from .models import Favorite

class IndexView(ListView):
    template_name = 'watchlist/index.html'
    context_object_name = 'cryptos'

    def get_queryset(self):
        return Favorite.objects.all()

def render_favorites(request):
    tickers = Favorite.objects.all()
    ticker_list = list(tickers)
    ticker_list_string = ""
    

    tickers_list = [x.ticker for x in ticker_list]
    for x in tickers_list:
        ticker_list_string += str(x)
        ticker_list_string += ","
    ticker_list_string = ticker_list_string[:-1]

    api = Api()
    thing = api.getQuotes(ticker_list_string)
    dict = {}
    for x in thing:
        dict.update(x)

    cryptos = Favorite.objects.all()
    context = {
        'cryptos': cryptos,
        'thing': dict
    }
    return render(request, 'watchlist/index.html', context)

def add_favorite(request):
    ticker = request.POST['ticker']
    name = request.POST['name']
    if ticker and name:
        new_fav = Favorite(name=name, ticker=ticker)
        new_fav.save()

    return render_favorites(request)

def remove_favorite(request, name):
    if name:
        thing = Favorite.objects.get(name=name)
        thing.delete()
    return render_favorites(request)


