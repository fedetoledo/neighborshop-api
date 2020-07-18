from django.urls import path, include
from api.views import createProduct, DetailProduct, HomeView, ProductUpdateView, ProductListView


urlpatterns = [
    path('todos/', ProductListView.as_view(), name='todos'),
    path('nuevo/', createProduct),
    path('editar/<int:pk>', ProductUpdateView.as_view(), name='editar'),
    path('detalle/<int:pk>', DetailProduct.as_view(), name="detalle"),
    path('',HomeView),
]
