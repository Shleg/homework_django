from django.core.management.base import BaseCommand
from hw2_app.models import Product
from django.utils import timezone

class Command(BaseCommand):
    help = 'Adds a new product'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('price', type=float)
        parser.add_argument('quantity', type=int)

    def handle(self, *args, **options):
        name = options['name']
        description = options['description']
        price = options['price']
        quantity = options['quantity']
        product = Product.objects.create(
            name=name,
            description=description,
            price=price,
            quantity=quantity,
            date_added=timezone.now()
        )
        self.stdout.write(self.style.SUCCESS(f'Successfully added product {product.id}'))
