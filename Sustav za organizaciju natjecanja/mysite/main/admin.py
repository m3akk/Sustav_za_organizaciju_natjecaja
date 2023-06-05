from django.contrib import admin
from .models import *


model_list = [Organizator, Sudionik, Natjecaj, Prijava]
admin.site.register(model_list)