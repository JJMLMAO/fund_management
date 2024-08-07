import json
import os
from django.core.management.base import BaseCommand, CommandParser
from funds.models import Fund

class Command(BaseCommand):
    help = 'Import funds data from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            default='funds.json',
            help='Path to the JSON file containing fund data'
        )

    def handle(self, *args, **options):
        file_path = options['file']
        
        if not os.path.exists(file_path):
            self.stderr.write(f'Error: The file {file_path} does not exist.')
            return
        
        with open(file_path, 'r') as file:
            data = json.load(file)

        for item in data:
            fund, created = Fund.objects.get_or_create(
                name=item.get('name'),
                defaults={
                    'description': item.get('description'),
                    'investment_type': item.get('investment_type'),
                    'current_nav': item.get('current_nav'),
                    'ytd_return': item.get('ytd_return'),
                }
            )
            if created:
                self.stdout.write(f'Created fund: {fund.name}')
            else:
                self.stdout.write(f'Fund already exists: {fund.name}')
            
        