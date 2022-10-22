from django.shortcuts import render
from django.views.generic import ListView
from core.erp.models import Category

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



#opost y get

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        return context


