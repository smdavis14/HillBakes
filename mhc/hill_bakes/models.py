from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField()

    def __str__(self):
        return self.username


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150, default='')

    def __str__(self):
        return self.name


class ProductType(models.Model):
    type = models.CharField(max_length=50)
    price = models.IntegerField()
    product = models.ManyToManyField(Product)

    def __str__(self):
        return self.type


class UserHistory(models.Model):
    type = models.ForeignKey(
        ProductType, on_delete=models.PROTECT, related_name='histories')
    quantity = models.IntegerField(default=0)
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name='histories')
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='histories')
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user
