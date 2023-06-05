
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login




# from django.contrib.auth.decorators import login_required






from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'registration/register.html', context)



from django.contrib.auth.forms import AuthenticationForm




from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            form.add_error(None, 'Your username and password didn\'t match. Please try again.')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})




from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout


def logout(request):
    auth_logout(request)
    return redirect('index')







def index(request):
    return render(request, 'index.html')











def organizator_list(request):
    organizatori = Organizator.objects.all()
    return render(request, 'organizatori/organizator_list.html', {'organizatori': organizatori})

def organizator_detail(request, pk):
    organizator = get_object_or_404(Organizator, pk=pk)
    return render(request, 'organizatori/organizator_detail.html', {'organizator': organizator})

def organizator_create(request):
    if request.method == 'POST':
        form = OrganizatorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('organizator_list')
    else:
        form = OrganizatorForm()
        print(form.errors)
    return render(request, 'organizatori/organizator_create.html', {'form': form})

def organizator_update(request, pk):
    organizator = get_object_or_404(Organizator, pk=pk)
    if request.method == 'POST':
        form = OrganizatorForm(request.POST, instance=organizator)
        if form.is_valid():
            form.save()
            return redirect('organizator_list')
    else:
        form = OrganizatorForm(instance=organizator)
    return render(request, 'organizatori/organizator_update.html', {'form': form})


def organizator_delete(request, pk):
    organizator = get_object_or_404(Organizator, pk=pk)
    if request.method == 'POST':
        form = OrganizatorDeleteForm(request.POST, instance=organizator)
        if form.is_valid():
            organizator.delete()
            return redirect('organizator_list')
    else:
        form = OrganizatorDeleteForm(instance=organizator)
    return render(request, 'organizatori/organizator_delete.html', {'organizator': organizator, 'form': form})


















def sudionik_list(request):
    sudionici = Sudionik.objects.all()
    return render(request, 'sudionici/sudionik_list.html', {'sudionici': sudionici})

def sudionik_detail(request, pk):
    sudionik = get_object_or_404(Sudionik, pk=pk)
    return render(request, 'sudionici/sudionik_detail.html', {'sudionik': sudionik})

def sudionik_create(request):
    if request.method == 'POST':
        form = SudionikForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sudionik_list')
    else:
        form = SudionikForm()
        print(form.errors)
    return render(request, 'sudionici/sudionik_create.html', {'form': form})



def sudionik_update(request, pk):
    sudionik = get_object_or_404(Sudionik, pk=pk)
    if request.method == 'POST':
        form = SudionikForm(request.POST, instance=sudionik)
        if form.is_valid():
            form.save()
            return redirect('sudionik_list')
    else:
        form = SudionikForm(instance=sudionik)
    return render(request, 'sudionici/sudionik_update.html', {'form': form})


def sudionik_delete(request, pk):
    sudionik = get_object_or_404(Sudionik, pk=pk)
    if request.method == 'POST':
        form = SudionikDeleteForm(request.POST, instance=sudionik)
        if form.is_valid():
            sudionik.delete()
            return redirect('sudionik_list')
    else:
        form = SudionikDeleteForm(instance=sudionik)
    return render(request, 'sudionici/sudionik_delete.html', {'sudionik': sudionik, 'form': form})

























def natjecaj_list(request):
    natjecaji = Natjecaj.objects.all()
    return render(request, 'natjecaji/natjecaj_list.html', {'natjecaji': natjecaji})


def natjecaj_detail(request, pk):
    natjecaj = get_object_or_404(Natjecaj, pk=pk)
    return render(request, 'natjecaji/natjecaj_detail.html', {'natjecaj': natjecaj})

def natjecaj_create(request):
    if request.method == 'POST':
        form = NatjecajForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('natjecaj_list')
    else:
        form = NatjecajForm()
    return render(request, 'natjecaji/natjecaj_create.html', {'form': form})


def natjecaj_update(request, pk):
    natjecaj = get_object_or_404(Natjecaj, pk=pk)
    if request.method == 'POST':
        form = NatjecajForm(request.POST, instance=natjecaj)
        if form.is_valid():
            form.save()
            return redirect('natjecaj_list')
    else:
        form = NatjecajForm(instance=natjecaj)
    return render(request, 'natjecaji/natjecaj_update.html', {'form': form})

def natjecaj_delete(request, pk):
    natjecaj = get_object_or_404(Natjecaj, pk=pk)
    if request.method == 'POST':
        form = NatjecajDeleteForm(request.POST, instance=natjecaj)
        if form.is_valid():
            natjecaj.delete()
            return redirect('natjecaj_list')
    else:
        form = NatjecajDeleteForm(instance=natjecaj)    
    return render(request, 'natjecaji/natjecaj_delete.html', {'natjecaj': natjecaj, 'form': form})
























def prijava_list(request):
    prijave = Prijava.objects.all()
    return render(request, 'prijave/prijava_list.html', {'prijave': prijave})



def prijava_detail(request, pk):
    prijava = get_object_or_404(Prijava, pk=pk)
    return render(request, 'prijave/prijava_detail.html', {'prijava': prijava})



def prijava_create(request):
    if request.method == 'POST':
        form = PrijavaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prijava_list')
    else:
        form = PrijavaForm()
        print(form.errors)
    return render(request, 'prijave/prijava_create.html', {'form': form})




def prijava_update(request, pk):
    prijava = get_object_or_404(Prijava, pk=pk)
    if request.method == 'POST':
        form = PrijavaForm(request.POST, instance=prijava)
        if form.is_valid():
            form.save()
            return redirect('prijava_list')
    else:
        form = PrijavaForm(instance=prijava)
    return render(request, 'prijave/prijava_update.html', {'form': form})



def prijava_delete(request, pk):
    prijava = get_object_or_404(Prijava, pk=pk)
    if request.method == 'POST':
        form = PrijavaDeleteForm(request.POST, instance=prijava)
        if form.is_valid():
            prijava.delete()
            return redirect('prijava_list')
    else:
        form = PrijavaDeleteForm(instance=prijava)    
    return render(request, 'prijave/prijava_delete.html', {'prijava': prijava, 'form': form})