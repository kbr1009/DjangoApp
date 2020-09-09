from django.shortcuts import render
from django.views import generic
from .models import Product
# Create your views here.

#class IndexView(generic.TemplateView):
#    template_name = 'front/index.html'

#    def get(self, request, *args, **kwargs):
#        products = Product.objects.all()
#        return render(request, self.template_name,{'products':products})

# listviewを使用した時

class IndexView(generic.Listview):
    template_name = 'front/index.html'
    modele = Product
