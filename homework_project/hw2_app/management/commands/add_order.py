from django.core.management.base import BaseCommand, CommandError
from hw2_app.models import Order, Client, Product, OrderItem
from django.utils import timezone


class Command(BaseCommand):
    help = 'Adds a new order'

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int)
        parser.add_argument('--products', nargs='+', type=int)

    def handle(self, *args, **options):
        client_id = options['client_id']
        products = options['products']

        if len(products) % 2 != 0:
            raise CommandError('Products input should be in pairs of product_id and quantity.')

        try:
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            raise CommandError('Client not found')

        total_amount = 0
        order_items = []
        for i in range(0, len(products), 2):
            product_id = products[i]
            quantity = products[i + 1]
            try:
                product = Product.objects.get(id=product_id)
                total_price = product.price * quantity
                total_amount += total_price
                order_items.append(OrderItem(product=product, quantity=quantity))
            except Product.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Product with ID {product_id} not found'))
                continue

        order = Order.objects.create(client=client, total_amount=total_amount, order_date=timezone.now())
        for item in order_items:
            item.order = order
            item.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully added order {order.id} with total amount ${total_amount}'))
