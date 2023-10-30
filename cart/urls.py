from django.contrib import admin
from django.urls import path, include
from cart.views import *

urlpatterns = [
    path('add/<int:product_id>',add_to_cart, name='addtocart' ),
    path('catt/', cart, name='cart'),
    path('delete/<product_id>', delete_product_cart, name='delete'),
]