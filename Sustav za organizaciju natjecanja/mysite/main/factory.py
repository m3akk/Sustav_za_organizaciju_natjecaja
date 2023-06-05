import factory
from factory.django import DjangoModelFactory
from .models import Organizator, Natjecaj, Sudionik, Prijava


class OrganizatorFactory(DjangoModelFactory):
    class Meta:
        model = Organizator

    organizator_naziv = factory.Faker('company')
    organizator_email = factory.Faker('email')




class SudionikFactory(DjangoModelFactory):
    class Meta:
        model = Sudionik

    sudionik_naziv = factory.Faker('name')
    sudionik_email = factory.Faker('email')



class NatjecajFactory(DjangoModelFactory):
    class Meta:
        model = Natjecaj

    natjecaj_naziv = factory.Faker('word')
    natjecaj_datum = factory.Faker('date')
    natjecaj_organizator = factory.Iterator(Organizator.objects.all())
    
    
    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        if not create or not extracted:
            # Simple build, or nothing to add, do nothing.
            return

        # Add the iterable of groups using bulk addition
        self.groups.add(*extracted)



class PrijavaFactory(DjangoModelFactory):
    class Meta:
        model = Prijava

    prijava_natjecaj = factory.Iterator(Natjecaj.objects.all())
    prijava_sudionik = factory.Iterator(Sudionik.objects.all())
    prijava_broj = factory.Faker('pyint')
