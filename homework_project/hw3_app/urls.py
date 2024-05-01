from django.urls import path
from .views import client_orders, client_form

urlpatterns = [
    path('', client_form, name='client-client_form'),
    path('client/<int:client_id>/orders/', client_orders, name='client-orders'),
]
