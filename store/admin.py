from django.contrib import admin
from store.models import *

admin.site.register([Category, Customer, Product, Order])