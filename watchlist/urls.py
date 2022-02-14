from django.urls import path

from . import views

app_name = 'watchlist'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('load-prices/', views.do_thing, name='load_prices')
]
