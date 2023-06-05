import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import *
from main.factory import *

NUM_ORGANIZATOR = 20
NUM_SUDIONIK = 20
NUM_NATJECAJ = 20
NUM_PRIJAVA = 20

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Organizator, Sudionik, Natjecaj, Prijava]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_ORGANIZATOR):
            mentor = OrganizatorFactory()

        for _ in range(NUM_SUDIONIK):
            kolegij = SudionikFactory()

        for _ in range(NUM_NATJECAJ):
            student = NatjecajFactory()

        for _ in range(NUM_PRIJAVA):
            zavrsni_rad = PrijavaFactory()