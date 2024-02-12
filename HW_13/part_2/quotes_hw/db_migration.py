import os
from django import setup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quotes_hw.settings")
setup()
from django.core.management.base import BaseCommand
from quotes_web_hw.models import Quote

class Command(BaseCommand):
    help = 'Перенесення даних із MongoDB у PostgreSQL'

    def handle(self, *args, **options):

        quotes_from_mongo = Quote.objects.all()


        for quote_mongo in quotes_from_mongo:
            Quote.objects.create(
                text=quote_mongo.text,
                author=quote_mongo.author,
                tags=quote_mongo.tags
            )

        self.stdout.write(self.style.SUCCESS('Дані успішно перенесені.'))