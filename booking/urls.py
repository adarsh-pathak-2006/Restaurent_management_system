from django.urls import path
from .views import AllTables, TableDetail, ReservationListAPI, ReservationCreateAPI, ReservationDetailAPI

urlpatterns = [
    path('table/', AllTables.as_view(), name='all_tables'),
    path('table/<int:pk>/', TableDetail.as_view(), name='table_detail'),
    path('reservation/', ReservationListAPI.as_view(), name='reservations'),
    path('reservation-create/', ReservationCreateAPI.as_view(), name='reservation_create'),
    path('reservation/<int:pk>/', ReservationDetailAPI.as_view(), name='reservation_detail'),
]
