from django.core.management.base import BaseCommand
from hw2_app.models import Order

class Command(BaseCommand):
    help = 'Displays information about an order'

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=int)

    def handle(self, *args, **options):
        order_id = options['order_id']
        try:
            order = Order.objects.get(id=order_id)
            order_items = order.orderitem_set.all()
            self.stdout.write(f"Order ID: {order.id}, Client: {order.client.name}, Order Date: {order.order_date}")
            for item in order_items:
                self.stdout.write(f"Product: {item.product.name}, Quantity: {item.quantity}, Price per unit: ${item.product.price}")
            self.stdout.write(f"Total Amount: ${order.total_amount}")
        except Order.DoesNotExist:
            self.stdout.write(self.style.ERROR('Order not found'))
