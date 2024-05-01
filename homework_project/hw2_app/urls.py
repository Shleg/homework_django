from django.urls import path
from .views import hw2, add_product, add_client

urlpatterns = [
    path('', hw2, name='hw2'),
    path('add_product/', add_product, name='add_product'),
    path('add_client/', add_client, name='add_client'),
]
