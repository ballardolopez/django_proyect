from django.test import TestCase

# Create your tests here.

from config.wsgi import *
# Create your tests here.
#from core.erp.models import Category



##uery = Category.objects.all()
#print(query)

from config.wsgi import *
from core.erp.models import *

data = ['Leche y derivados', 'Carnes, pescados y huevos', 'Patatas, legumbres, frutos secos',
        'Verduras y Hortalizas', 'Frutas', 'Cereales y derivados, azúcar y dulces',
        'Grasas, aceite y mantequilla']

for i in data:
    cat = Category(name=i)
    cat.save()
    print('Guardado registro N°{}'.format(cat.id))

