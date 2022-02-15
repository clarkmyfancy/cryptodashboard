from django.urls import path

from . import views

app_name = 'watchlist'
urlpatterns = [
    path('', views.render_favorites, name='index'),
    path('add-favorite/', views.add_favorite, name="add_favorite"),
    path('remove-favorite/<str:name>/', views.remove_favorite, name='remove_favorite')
]
