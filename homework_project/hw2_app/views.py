import logging
from django.shortcuts import render
from .forms import ProductForm, ClientForm
from .models import Product, Client

logger = logging.getLogger(__name__)


def hw2(request):
    return render(request, 'hw2_app/hw2.html')


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            date_added = form.cleaned_data['date_added']
            logger.info(f'Продукт:'
                        f' {name=}, '
                        f'{description=}, '
                        f'{price=}.'
                        f'{quantity=}.'
                        f'{date_added=}.')

            product = Product(name=name,
                              description=description,
                              price=price,
                              quantity=quantity,
                              date_added=date_added)
            product.save()
            message = 'Продукт сохранён в базе данных'
    else:
        form = ProductForm()
        message = 'Заполните форму'

    return render(request, 'hw2_app/add_product.html', {'form': form, 'message': message})


def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            registration_date = form.cleaned_data['registration_date']
            logger.info(f'Клиент:'
                        f' {name=}, '
                        f'{email=}, '
                        f'{phone_number=}.'
                        f'{address=}.'
                        f'{registration_date=}.')

            client = Client(name=name,
                            email=email,
                            phone_number=phone_number,
                            address=address,
                            registration_date=registration_date)
            client.save()
            message = 'Клиент сохранён в базе данных'
    else:
        form = ClientForm()
        message = 'Заполните форму'

    return render(request, 'hw2_app/add_client.html', {'form': form, 'message': message})
