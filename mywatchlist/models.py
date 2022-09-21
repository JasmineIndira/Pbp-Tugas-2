from django.db import models
from unicodedata import decimal

# Create your models here.
class MyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=5, decimal_places=1)
    release_date = models.DateField()
    review = models.TextField()
