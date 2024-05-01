from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm, ProductId
from .models import Product

import logging

logger = logging.getLogger(__name__)


def home(request):
    if request.method == 'POST':
        form = ProductId(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data['product_id']
            return redirect('edit_product', product_id=product_id)
    else:
        form = ProductId()
    return render(request, 'hw4_app/hw4.html', {'form': form})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            product = form.save()  # Эта строка сохраняет все данные формы, включая файл изображения
            logger.info(
                f'Продукт добавлен: {product.name}, Описание: {product.description}, Цена: {product.price}, Количество: {product.quantity}, Дата добавления: {product.date_added}, Изображение: {product.image.url if product.image else "No image"}')

        message = 'Продукт сохранён в базе данных'
    else:
        form = ProductForm()
        message = 'Заполните форму'

    return render(request, 'hw4_app/add_product.html', {'form': form, 'message': message})


def edit_product(request, product_id=None):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Предполагаем, что есть URL с именем 'product_list'
    else:
        form = ProductForm(instance=product)
    return render(request, 'hw4_app/product_form.html', {'form': form})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'hw4_app/product_list.html', {'products': products})