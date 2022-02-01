from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('dashboard.urls')),
    path('cryptos/', include('cryptos.urls')),
    path('admin/', admin.site.urls),
]
