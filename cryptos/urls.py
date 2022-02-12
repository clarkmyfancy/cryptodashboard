from django.urls import path

from . import views

app_name = 'cryptos'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add-favorite/', views.add_favorite, name="add_favorite"),
    path('remove-from-watchlist/', views.remove_from_watchlist, name="remove_from_watchlist"),
    path('<slug:ticker>/', views.DetailView.as_view(), name="get_single_crypto"),
]
