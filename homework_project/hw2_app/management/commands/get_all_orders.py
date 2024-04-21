from django.core.management.base import BaseCommand
from hw2_app.models import Order, OrderItem

class Command(BaseCommand):
    help = 'Displays information about all orders'

    def handle(self, *args, **options):
        orders = Order.objects.all()
        if not orders:
            self.stdout.write(self.style.WARNING('No orders found'))
            return

        for order in orders:
            self.stdout.write(self.style.SUCCESS(f"Order ID: {order.id}, Client: {order.client.name}, Order Date: {order.order_date.strftime('%Y-%m-%d')}, Total Amount: ${order.total_amount}"))
            order_items = order.orderitem_set.all()
            if order_items:
                for item in order_items:
                    self.stdout.write(f"    Product: {item.product.name}, Quantity: {item.quantity}, Price per unit: ${item.product.price}")
            else:
                self.stdout.write(self.style.ERROR('    No products found for this order'))
            self.stdout.write("\n")  # Adds a newline for better readability
