from django.db import models

# Create your models here.
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    year = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    image = models.CharField(max_length=255)