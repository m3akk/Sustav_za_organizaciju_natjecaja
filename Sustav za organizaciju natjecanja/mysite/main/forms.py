from django import forms
from .models import *




class OrganizatorForm(forms.ModelForm):
    class Meta:
        model = Organizator
        fields = ['organizator_naziv', 'organizator_email']
        widgets = {
            'organizator_naziv': forms.TextInput(attrs={'class': 'form-control'}),
            'organizator_email': forms.TextInput(attrs={'class': 'form-control'}),
        }

class OrganizatorDeleteForm(forms.ModelForm):
    class Meta:
        model = Organizator
        fields = []



class SudionikForm(forms.ModelForm):
    class Meta:
        model = Sudionik
        fields = ['sudionik_naziv', 'sudionik_email']
        widgets = {
            'sudionik_naziv': forms.TextInput(attrs={'class': 'form-control'}),
            'sudionik_email': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SudionikDeleteForm(forms.ModelForm):
    class Meta:
        model = Sudionik
        fields = []




class NatjecajForm(forms.ModelForm):
    class Meta:
        model = Natjecaj
        fields = ['natjecaj_naziv', 'natjecaj_datum', 'natjecaj_organizator', 'natjecaj_sudionici']
        widgets = {
            'natjecaj_naziv': forms.TextInput(attrs={'class': 'form-control'}),
            'natjecaj_datum': forms.DateInput(attrs={'class': 'form-control'}),
            'natjecaj_organizator': forms.Select(attrs={'class': 'form-control'}),
            'natjecaj_sudionici': forms.CheckboxSelectMultiple(),
        }

class NatjecajDeleteForm(forms.ModelForm):
    class Meta:
        model = Natjecaj
        fields = []





class PrijavaForm(forms.ModelForm):
    class Meta:
        model = Prijava
        fields = ['prijava_broj', 'prijava_natjecaj', 'prijava_sudionik']
        widgets = {
            'prijava_broj': forms.NumberInput(attrs={'class': 'form-control'}),
            'prijava_natjecaj': forms.Select(attrs={'class': 'form-control'}),
            'prijava_sudionik': forms.Select(attrs={'class': 'form-control'})
        }

class PrijavaDeleteForm(forms.ModelForm):
    class Meta:
        model = Prijava
        fields = []