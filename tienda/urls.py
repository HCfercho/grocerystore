from django.urls import path
from . import views

urlpatterns = [
    path('product-list/', views.product_list, name="product-list"),
    path('tienda-uno-list/', views.tienda1_list, name='tienda-uno-list'),
    path('tienda-dos-list/', views.tienda2_list, name='tienda-dos-list'),
    path('tienda-tres-list/', views.tienda3_list, name='tienda-tres-list'),
    path('tienda-cuatro-list/', views.tienda4_list, name='tienda-cuatro-list'),
    path('stock/', views.stock_en_tienda_list, name='stock'),
    path('categorias/', views.categoria_list, name='categorias'),
    path('subcategorias/', views.subcategoria_list, name='subcategorias'),
]
