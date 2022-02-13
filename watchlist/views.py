from django.views.generic import ListView

from .models import Favorite

class IndexView(ListView):
    template_name = 'cryptos/index.html'
    context_object_name = 'cryptos'

    def get_queryset(self):
        return Favorite.objects.all()