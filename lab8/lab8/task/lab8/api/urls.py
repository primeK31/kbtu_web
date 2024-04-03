from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list,),
    path("products/<int:id>", views.get_product,),
    path('categories/', views.category_list,), 
    path('categories/<int:id>', views.get_category,), 
    path('categories/<int:id>/products/', views.get_products_from_category,)
]

