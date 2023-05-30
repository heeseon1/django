from django.db import models

# Create your models here.

class Book(models.Model):
    bid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=20)
    category = models.CharField(max_length=30)
    price = models.IntegerField()
    published_date = models.DateField()
    description = models.TextField()
