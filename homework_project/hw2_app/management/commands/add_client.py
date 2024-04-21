from django.core.management.base import BaseCommand
from hw2_app.models import Client


class Command(BaseCommand):
    help = 'Adds a new client'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('phone_number', type=str)
        parser.add_argument('address', type=str)

    def handle(self, *args, **options):
        name = options['name']
        email = options['email']
        phone_number = options['phone_number']
        address = options['address']
        client = Client.objects.create(name=name, email=email, phone_number=phone_number, address=address)
        self.stdout.write(self.style.SUCCESS(f'Successfully added client {client.id}'))
