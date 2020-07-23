from django.urls import path, include
from .views import (profileView, UserLoginView, 
    createProduct, DetailProduct, HomeView, 
    ProductUpdateView, ProductListView, CreateUserView)

urlpatterns = [
    path('todos/', ProductListView.as_view(), name='todos'),
    path('nuevo/', createProduct),
    path('editar/<int:pk>', ProductUpdateView.as_view(), name='editar'),
    path('detalle/<int:pk>', DetailProduct.as_view(), name="detalle"),
    path('',HomeView, name='home'),
    path('login', UserLoginView.as_view(), name='login'),
    path('signup', CreateUserView.as_view(), name='signup'),
    path('profile', profileView, name='profile'),
]
