from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
import random
from hw3_app.models import Client, Product, Order, OrderItem

class Command(BaseCommand):
    help = 'Fills the database with test data'

    def add_arguments(self, parser):
        # parser.add_argument('--clients', type=int, help='The number of clients to create')
        # parser.add_argument('--products', type=int, help='The number of products to create')
        parser.add_argument('--orders', type=int, help='The number of orders to create')

    def handle(self, *args, **options):
        #
        # self.create_clients(options.get('clients', 10))
        # self.create_products(options.get('products', 15))
        self.create_orders(options.get('orders', 20))
        self.stdout.write(self.style.SUCCESS('Database populated with test data'))

    # def create_clients(self, n):
    #     for i in range(n):
    #         Client.objects.create(
    #             name=f"Клиент {i+1}",
    #             email=f"client{i+1}@example.com",
    #             phone_number=f"+7903123456{i+1}",
    #             address=f"Адрес {i+1}",
    #             registration_date=timezone.now() - timedelta(days=random.randint(1, 365))
    #         )

    # def create_products(self, n):
    #     for i in range(n):
    #         Product.objects.create(
    #             name=f"Продукт {i+1}",
    #             description=f"Описание продукта {i+1}",
    #             price=random.randint(100, 1000),
    #             quantity=random.randint(1, 50),
    #             date_added=timezone.now() - timedelta(days=random.randint(1, 365))
    #         )

    def create_orders(self, n):
        clients = list(Client.objects.all())
        products = list(Product.objects.all())

        for i in range(n):
            client = random.choice(clients)
            order = Order.objects.create(
                client=client,
                total_amount=random.randint(1000, 5000),
                order_date=timezone.now() - timedelta(days=random.randint(1, 3))
            )

            for _ in range(random.randint(1, 5)):
                product = random.choice(products)
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=random.randint(1, 3)
                )
