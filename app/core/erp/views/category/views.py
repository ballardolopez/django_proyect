from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from core.erp.forms import CategoryForm
from core.erp.models import Category
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

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
       # data = {'name': 'Edin'}
       data = {}
       print(request.POST)
       try:
           data = Category.objects.get(pk=request.POST['id']).toJSON()
       except Exception as e:
           data['error'] = str(e)
       return JsonResponse(data)

#opost y get

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        return context



class CategoryCreateView(CreateView):
   model = Category
   form_class = CategoryForm
   template_name = 'category/create.html'
   success_url = reverse_lazy('erp:category_list')

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['title'] = 'Creación una Categoria'
       return context
