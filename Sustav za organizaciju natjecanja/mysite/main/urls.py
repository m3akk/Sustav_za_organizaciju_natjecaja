from django.urls import path
from . import views
from main.views import *

urlpatterns = [

    # path('', views.homepage, name='homepage'),


    path('', views.index, name='index'),

    path('accounts/login/', views.login_view, name='login'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/logout/', views.logout, name='logout'),

    path('organizatori/', views.organizator_list, name='organizator_list'),
    path('organizatori/create/', views.organizator_create, name='organizator_create'),
    path('organizatori/<int:pk>/', views.organizator_detail, name='organizator_detail'),
    path('organizatori/<int:pk>/update/', views.organizator_update, name='organizator_update'),
    path('organizatori/<int:pk>/delete/', views.organizator_delete, name='organizator_delete'),

    path('sudionici/', views.sudionik_list, name='sudionik_list'),
    path('sudionici/create/', views.sudionik_create, name='sudionik_create'),
    path('sudionici/<int:pk>/', views.sudionik_detail, name='sudionik_detail'),
    path('sudionici/<int:pk>/update/', views.sudionik_update, name='sudionik_update'),
    path('sudionici/<int:pk>/delete/', views.sudionik_delete, name='sudionik_delete'),

    path('natjecaji/', views.natjecaj_list, name='natjecaj_list'),
    path('natjecaji/create/', views.natjecaj_create, name='natjecaj_create'),
    path('natjecaji/<int:pk>/', views.natjecaj_detail, name='natjecaj_detail'),
    path('natjecaji/<int:pk>/update/', views.natjecaj_update, name='natjecaj_update'),
    path('natjecaji/<int:pk>/delete/', views.natjecaj_delete, name='natjecaj_delete'),

    path('prijave/', views.prijava_list, name='prijava_list'),
    path('prijave/create/', views.prijava_create, name='prijava_create'),
    path('prijave/<int:pk>/', views.prijava_detail, name='prijava_detail'),
    path('prijave/<int:pk>/update/', views.prijava_update, name='prijava_update'),
    path('prijave/<int:pk>/delete/', views.prijava_delete, name='prijava_delete'),


]


