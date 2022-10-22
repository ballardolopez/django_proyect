from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from core.erp.models import Category
from django.utils.decorators import method_decorator

def category_list(request):
#json
    data = {

        #mandarlo como parametro
        'title': 'Listado de Categorías',
        'categories': Category.objects.all()
    }
    return render(request, 'category/list.html', data)

class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'

    #@method_decorator(login_required):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
       # if request.method == 'GET':
            #llamar el metodo redirect, redireccionar
        #    return redirect('erp:category_list2')
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {'name': 'Edin'}
        return JsonResponse(data)

#opost y get

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        return context

