from django.test import TestCase
#importar el codigo de wsgi , con asterisco todo

from config.wsgi import *
# Create your tests here.
from core.erp.models import Tipo


#ORM SCRIPS - PODEROSO DJANGO

#query = Tipo.objects.all()
#print(query)

#insercion de datos

#t = Tipo()

#t.name = 'Accionista'
#t.save

#otra forma
#t = Tipo(name='Presidente').save()

#Edicion de Datos, se puede poner id o pk

#t = Tipo.objects.get(pk=1)
#print(t.name)

  #eliminacion
#t = Tipo.objects.get(pk=1).delete()


#tambien se puede con try catch a datos repetidos



#listar, con filtro en este caso los que inician, contieene, etc

#obj = Tipo.objects.filter(nombre__contains='pre') # contiene
#obj = Tipo.objects.filter(nombre__startswith='pre')#inician con
#print(obj)


#for i in Tipo.objects.filter(nombre__endswith='a'):
 #   print(i.nombre)