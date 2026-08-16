from django.urls import path
from .views import MenuAPI, MenuRetrieveAPI, OrderAPI, OrderCreateAPI, OrderDetailAPI

urlpatterns = [
    path('menu/', MenuAPI.as_view(), name='menu'),
    path('menu/<int:pk>/', MenuRetrieveAPI.as_view(), name='menu_detail'),
    path('order/', OrderAPI.as_view(), name='order'),
    path('order/<int:pk>/', OrderDetailAPI.as_view(), name='order_detail'),
    path('order-create/', OrderCreateAPI.as_view(), name='order_create'),
]
