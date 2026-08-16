from rest_framework.permissions import BasePermission
from django.contrib.auth import get_user_model

User=get_user_model()

class IsManager(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.role=='MANAGER')

class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.role=='CUSTOMER')        