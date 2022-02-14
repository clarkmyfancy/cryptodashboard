from django.views.generic import ListView
from django.shortcuts import render

from coinmarketcap_api.api import Api

from .models import Favorite

class IndexView(ListView):
    template_name = 'watchlist/index.html'
    context_object_name = 'cryptos'

    def get_queryset(self):
        return Favorite.objects.all()

def do_thing(request):
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
