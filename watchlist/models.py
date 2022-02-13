from django.db import models

class Favorite(models.Model):
    ticker = models.CharField(max_length=5)
    name = models.CharField(max_length=50)