from django.db import models




class Organizator(models.Model):
    organizator_naziv = models.CharField(max_length=255)
    organizator_email = models.EmailField()

    def __str__(self):
        return str(self.organizator_naziv)
    


class Sudionik(models.Model):
    sudionik_naziv = models.CharField(max_length=255)
    sudionik_email = models.EmailField()

    def __str__(self):
        return str(self.sudionik_naziv)
    


class Natjecaj(models.Model):
    natjecaj_naziv = models.CharField(max_length=255)
    natjecaj_datum = models.DateField()
    natjecaj_organizator = models.ForeignKey(Organizator, on_delete=models.CASCADE, related_name='natjecaji')
    natjecaj_sudionici = models.ManyToManyField(Sudionik, related_name='natjecaji')

    def __str__(self):
        return str(self.natjecaj_naziv)


class Prijava(models.Model):
    prijava_broj = models.IntegerField()
    prijava_natjecaj = models.ForeignKey(Natjecaj, on_delete=models.CASCADE, related_name='prijave')
    prijava_sudionik = models.OneToOneField(Sudionik, on_delete=models.CASCADE, related_name='prijava')

    def __str__(self):
        return str(self.prijava_broj)