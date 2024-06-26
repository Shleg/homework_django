from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta

from .models import Order, Product
from .forms import ClientId


def client_form(request):
    if request.method == 'POST':
        form = ClientId(request.POST)
        if form.is_valid():
            client_id = form.cleaned_data['client_id']
            return client_orders(request, client_id)

    else:
        form = ClientId()

    return render(request, 'hw3_app/client_id.html', {'form': form})


def client_orders(request, client_id):
    today = timezone.now()
    context = {
        'products_week': unique_products(client_id, today - timedelta(days=7)),
        'products_month': unique_products(client_id, today - timedelta(days=30)),
        'products_year': unique_products(client_id, today - timedelta(days=365)),
    }
    return render(request, 'hw3_app/client_orders.html', context)


def unique_products(client_id, date_from):
    orders = Order.objects.filter(client_id=client_id, order_date__gte=date_from)
    product_ids = set()
    for order in orders:
        product_ids.update(order.products.values_list('id', flat=True))
    return Product.objects.filter(id__in=product_ids)
