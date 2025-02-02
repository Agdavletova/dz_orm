import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from datetime import datetime
from django.utils.text import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        # for phone in phones:
        #     Phone.objects.create(name=phone['name'], image=phone['image'], price=int(phone['price']), release_date=datetime.strptime(phone['release_date'], "%Y-%m-%d").date(), lte_exists=bool(phone['lte_exists']), slug=slugify(phone['name']))
        phones = [f"{c.id} {c.name}, {c.price} {c.slug}" for c in Phone.objects.all()]
        print(phones)
