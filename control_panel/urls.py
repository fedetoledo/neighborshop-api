from django.urls import path, include
from .views import (profileView, UserLoginView, ProductDeleteView,
    createProduct, DetailProduct, HomeView, logoutView,
    ProductUpdateView, ProductListView, CreateUserView)

urlpatterns = [
    # path('todos/', ProductListView.as_view(), name='todos'),
    path('',HomeView, name='home'),
    path('logout', logoutView, name='logout'),
    path('tienda/login', UserLoginView.as_view(), name='login'),
    path('tienda/signup', CreateUserView.as_view(), name='signup'),
    path('tienda/producto/detalle/<int:pk>', DetailProduct.as_view(), name="detalle"),
    path('tienda/producto/nuevo/', createProduct),
    path('tienda/producto/editar/<int:pk>', ProductUpdateView.as_view(), name='editar'),
    path('tienda/producto/eliminar/<int:pk>', ProductDeleteView.as_view(), name='eliminar'),
    path('tienda/', profileView, name='tienda'),
]
