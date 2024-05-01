from django.urls import path
from .views import add_product, edit_product, home, product_list

urlpatterns = [
    path('', home, name='home'),
    path('product/add/', add_product, name='add_product'),
    path('product/<int:product_id>/edit/', edit_product, name='edit_product'),
    path('products/', product_list, name='product_list'),
]
