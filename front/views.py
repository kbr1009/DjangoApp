from django.shortcuts import render
from django.views import generic
from .models import Product
# Create your views here.

#class IndexView(generic.TemplateView): # # templateviewはデータベースがない時に使用
#    template_name = 'front/index.html'

#    def get(self, request, *args, **kwargs):
#        products = Product.objects.all()
#        return render(request, self.template_name,{'products':products})

class IndexView(generic.ListView): #Listviewを使用した時
    template_name = 'front/index.html'
    model = Product

    def get_queryset(self):# （検索機能）　https://www.youtube.com/watch?v=37y8P1jmvMU&list=PL8EQJPo_jL6uwdvohYo4CWWheonZPNuE6&index=5
        queryset = Product.objects.all()#上のyoutubeの4：00台を参照
        if 'query'in self.request.GET:
            qs = self.request.GET['query']
            queryset = queryset.filter(product_name=qs)
        return queryset


class ProductsDetail(generic.DetailView):
    template_name = 'front/detail.html'
    model = Product
