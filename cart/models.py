from django.db import models
from store.models import *



class Cart(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField()
  user = models.ForeignKey(Customer, on_delete=models.CASCADE)
