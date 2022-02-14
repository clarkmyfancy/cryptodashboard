from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from django.conf import settings


class Api:

    def __init__(self):

        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': settings.COINMARKETCAP_API_KEY,
        }
        self.session = Session()
        self.session.headers.update(self.headers)

    def getQuotes(self, cryptos_of_interest):

        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'  
        
        parameters = {
            'symbol': cryptos_of_interest
        }
        try:
            response = self.session.get(url, params=parameters)
            data = json.loads(response.text)
            return self.parse_out_tickers_and_prices(data, cryptos_of_interest)
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
        
    
    def parse_out_tickers_and_prices(self, data, cryptos_of_interest):
        tickers = cryptos_of_interest.split(",")
        thing = []
        for ticker in tickers:
            x = self.format_ticker_and_price(data, ticker)
            thing.append(x)
        return thing
            
    
    def format_ticker_and_price(self, data, ticker):
        price = data['data'][ticker]['quote']['USD']['price']
        price_truncated = round(price, 2)
        return dict([(ticker, price_truncated)])