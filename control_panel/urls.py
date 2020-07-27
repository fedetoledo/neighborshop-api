from django.urls import path, include

from .views.product_views import (
    createProductView, ProductUpdateView, ProductDetailView, ProductDeleteView
)
from .views.user_views import (
    UserLoginView, CreateUserView, profileView, logoutView
)
from .views.main_views import HomeView
from .views.market_views import MarketCreateView, MarketDeleteView, MarketDetailView

urlpatterns = [
    # path('todos/', ProductListView.as_view(), name='todos'),
    path('',HomeView, name='home'),
    path('logout', logoutView, name='logout'),
    path('tienda/login', UserLoginView.as_view(), name='login'),
    path('tienda/signup', CreateUserView.as_view(), name='signup'),
    path('tienda/crear', MarketCreateView.as_view(), name='nueva-tienda'),
    path('tienda/detalle/<int:pk>', MarketDetailView.as_view(), name='detalle-tienda'),
    path('tienda/eliminar/<int:pk>', MarketDeleteView.as_view(), name='eliminar-tienda'),
    path('tienda/producto/detalle/<int:pk>', ProductDetailView.as_view(), name="detalle"),
    path('tienda/producto/nuevo/', createProductView, name='nuevo'),
    path('tienda/producto/editar/<int:pk>', ProductUpdateView.as_view(), name='editar'),
    path('tienda/producto/eliminar/<int:pk>', ProductDeleteView.as_view(), name='eliminar'),
    path('tienda/', profileView, name='tienda'),
]
