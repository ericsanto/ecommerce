from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from store.models import *
from store.form import ProductForm, UserForm, CategoryForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse_lazy

def home(request):
  products = Product.objects.all()
  return render(request, 'home.html', {'products': products})

def add_products(request):
  if str(request.method) == 'POST':
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
      messages.success(request, 'O produto foi adicionado na base de dados')
      form.save()
      form = ProductForm()
    else:
      messages.error(request, 'Não foi possível adicionar o produto na base de dados')
  else:
    form = ProductForm()
  context = {'form': form }
  return render(request, 'addproducts.html', context)



def about(request):
  return render(request, 'about.html')




class RegisterUser(CreateView):
  template_name = 'registernewuser.html'
  form_class = UserForm
  success_url = reverse_lazy('home')



def product_details(request, pk):
  product = Product.objects.get(id=pk)
  return render(request, 'product.html',{'product': product})



def add_category(request):
  if str(request.method) == 'POST':
    form = CategoryForm(request.POST)
    if form.is_valid():
      form.save()
      form = CategoryForm()
    else:
      messages.error(request, 'Não foi possível adicionar essa categoria')
  else:
    form = CategoryForm()
  context = {'form': form}
  return render(request, 'addcategory.html', context)  


def update_product(request, product_id):
  product = Product.objects.get(pk=product_id)
  form = ProductForm(request.POST, request.FILES, instance=product)
  if form.is_valid():  
    form.save()
    return redirect('home')
  return render(request, 'update.html', {'form': form, 'product': product})



def categories(request, foo):
  foo = foo.replace('-', ' ')
  try:
    category = Category.objects.get(name=foo)
    products = Product.objects.filter(name=category)
    context = {'category': category, 'products': products}
    return render(request, 'category.html', context)
  except: 
    messages.success(request, 'Categoria não existe')
    return redirect('home')