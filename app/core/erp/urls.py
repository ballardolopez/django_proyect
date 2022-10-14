from django.contrib import admin
from django.urls import path
from core.erp.views import miprimeravista, misegundavista

app_name = 'erp'
urlpatterns = [
    path('uno/', miprimeravista, name='Vista1'),
    path('dos/', misegundavista, name='Vista2')
    ]
