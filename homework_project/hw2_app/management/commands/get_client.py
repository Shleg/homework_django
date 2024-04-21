from django.core.management.base import BaseCommand
from hw2_app.models import Client


class Command(BaseCommand):
    help = 'Displays information about a client'

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int)

    def handle(self, *args, **options):
        client_id = options['client_id']
        try:
            client = Client.objects.get(id=client_id)
            self.stdout.write(f"Client ID: {client.id}, Name: {client.name}, Email: {client.email}")
        except Client.DoesNotExist:
            self.stdout.write(self.style.ERROR('Client not found'))
