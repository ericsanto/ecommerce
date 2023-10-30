from django import forms
from store import models
from store.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class ProductForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = ['name', 'price','is_sale','sale_price' ,'category', 'descirption', 'image']



class UserForm(UserCreationForm):
  email = models.CharField(max_length=200)

  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'username', 'email']


    def clean_email(self):
      email = self.cleaned_data['email']
      if User.objects.filter(email=email).exists():
        raise ValidationError(f'O email {email} já está em uso')
      return email


class CategoryForm(forms.ModelForm):
  
  class Meta:
    model = Category
    fields = ['name']