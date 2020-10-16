from django.urls import path, include

from .views.product_views import (
    ProductUpdateView, ProductDetailView, ProductDeleteView, ProductCreateView
)
from .views.user_views import (
    UserLoginView, CreateUserView, marketView, logoutView
)
from .views.main_views import HomeView
from .views.market_views import MarketCreateView, MarketDeleteView, MarketDetailView, MarketUpdateView

urlpatterns = [
    path('',HomeView, name='home'),
    path('logout', logoutView, name='logout'),
    path('tienda/login', UserLoginView.as_view(), name='login'),
    path('tienda/signup', CreateUserView.as_view(), name='signup'),
    
    path('tienda/crear', MarketCreateView.as_view(), name='market-create'),
    path('tienda/detalle/<int:pk>', MarketDetailView.as_view(), name='market-detail'),
    path('tienda/editar/<int:pk>', MarketUpdateView.as_view(), name='market-edit'),
    path('tienda/eliminar/<int:pk>', MarketDeleteView.as_view(), name='market-delete'),
    
    path('tienda/producto/detalle/<int:pk>', ProductDetailView.as_view(), name="product-detail"),
    path('tienda/producto/nuevo/', ProductCreateView.as_view(), name='product-create'),
    path('tienda/producto/editar/<int:pk>', ProductUpdateView.as_view(), name='product-edit'),
    path('tienda/producto/eliminar/<int:pk>', ProductDeleteView.as_view(), name='product-delete'),

    path('tienda/', marketView, name='market'),
]
