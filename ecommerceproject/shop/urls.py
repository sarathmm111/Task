from django.contrib import admin
from django.urls import path, include
from shop import views

app_name = 'shop'

urlpatterns = [
    path('', views.AllprodCat, name='AllprodCat'),
    path('<slug:c_slug>/', views.AllprodCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.ProdDetail, name='products_category_detail'),

]
