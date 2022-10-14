#from django.http import JsonResponse
from django.shortcuts import render

from core.erp.models import Category, Product


#from django.http import HttpResponse
# Create your views here.

#vista basada en funcion, hay tambien basada en clase
def miprimeravista(request):

    data = {
    'name': 'Edin Eliceo',
    'categorias': Category.objects.all()
    }
    #return JsonResponse(data)
    return render(request, 'index.html', data);

    #return HttpResponse('Este es mi primera url')




#segunda lista

def misegundavista(request):

    data = {
    'name': 'Edin Eliceo',
    'productos': Product.objects.all()
    }
    #return JsonResponse(data)
    return render(request, 'index.html', data);