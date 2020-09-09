from django.urls import path
from . import views

app_name = 'front'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('detail/<int:pk>',views.ProductsDetail.as_view(),name='detail'), #<int:pk>のpkはプライマリキーの略
    #path('/products/',views.IndexView.as_view(),name='product-list')#youtube　しょう先生の【Python Webアプリ 中級】#5 の検索機能参照
]
