from django.contrib import admin
from django.urls import path
from core.erp.views.category.views import *

#from core.erp.views import miprimeravista, misegundavista

app_name = 'erp'
urlpatterns = [
    #path('uno/', miprimeravista, name='Vista1'),
    #path('dos/', misegundavista, name='Vista2')

    #path('category/list', category_list, name='category_list'),
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/list2/', category_list, name='category_list2'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),


    ]
