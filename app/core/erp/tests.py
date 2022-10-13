from django.test import TestCase

# Create your tests here.

from config.wsgi import *
# Create your tests here.
from core.erp.models import Category



query = Category.objects.all()
print(query)
