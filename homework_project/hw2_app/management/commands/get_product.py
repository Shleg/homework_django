from django.core.management.base import BaseCommand
from hw2_app.models import Product

class Command(BaseCommand):
    help = 'Displays information about a product'

    def add_arguments(self, parser):
        parser.add_argument('product_id', type=int)

    def handle(self, *args, **options):
        product_id = options['product_id']
        try:
            product = Product.objects.get(id=product_id)
            self.stdout.write(f"Product ID: {product.id}, Name: {product.name}, Price: ${product.price}, Quantity: {product.quantity}")
        except Product.DoesNotExist:
            self.stdout.write(self.style.ERROR('Product not found'))
