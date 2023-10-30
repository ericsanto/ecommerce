
from django.contrib import admin
from django.urls import path
from .views import *
from ecomm import settings 
from django.conf.urls.static import static
from django.contrib.auth  import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('addproduct/', add_products, name='addproducts'),
    path('about/', about, name='about'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout'), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('product/<int:pk>', product_details, name='product'),
    path('addcategory/', add_category, name='addcategory'),
    path('update_product/<product_id>', update_product , name='update'),
    path('category/<str:foo>', categories, name='category'),
] 