from rest_framework import permissions
from .models import Market

class IsLoggedInUserOrAdmin(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_staff

class IsAdminUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_staff

class IsSellerOrAdmin(permissions.BasePermission):
    message = 'You need to be a seller and own the market to perform this action'

    def has_permission(self, request, view):
        market = Market.objects.get(owner=request.user)
        return (request.user.is_seller and request.data['market'] == market.id) or request.user.is_staff