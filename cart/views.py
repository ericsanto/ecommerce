from django.shortcuts import render, redirect
from store.models import *
from cart.models import *


def cart(request):
  cart_items = Cart.objects.filter(user=Customer())
  context = {
    'cart_items': cart_items
  }
  return render(request, 'cart.html', context)



def add_to_cart(request, product_id):
  product = Product.objects.get(pk=product_id)
  if str(request.method) == 'POST':
    quantity = request.POST.get('quantity', 1)
    car_item, created = Cart.objects.get_or_create(product=product, user=request.user)
    car_item.quantity += (quantity)
    car_item.save()
  return redirect('cart')



def delete_product_cart(request, product_id):
  cart_items = Product.objects.get(pk=product_id)
  cart_items.delete()
  return redirect('cart')



 
