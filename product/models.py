from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Category(models.Model):
    title = models.CharField(default='', max_length=255)
    slug = models.CharField(default='', max_length=255)
    description = models.TextField(default="")
    active = models.BooleanField(default=True)


class Product(models.Model):
    title = models.CharField(default='', max_length=255)
    description = models.TextField(default="")
    active = models.BooleanField(default=True)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=CASCADE)
    title = models.CharField(default='', max_length=255)
    price = models.IntegerField(default=0)
    sale_price = models.IntegerField(default=0)
    inventory = models.IntegerField(default=0)
    active = models.BooleanField(default=True)