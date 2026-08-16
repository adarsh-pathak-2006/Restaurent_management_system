from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Reservation, Table
from .serializers import TableGetSerializer, TableSerializer, ReservationSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from config.permissions import IsCustomer, IsManager
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from config.throttling import TokenObtainThrottle, TokenRefreshThrottle, GeneralThrottle

class CustomTokenObtain(TokenObtainPairView):
    throttle_classes=[TokenObtainThrottle]

class CustomTokenRefresh(TokenRefreshView):
    throttle_classes=[TokenRefreshThrottle]

class AllTables(ListCreateAPIView):
    throttle_classes=[GeneralThrottle]
    def get_permissions(self):
        if self.request.method=="GET":
            return [IsAuthenticated()]
        return [IsManager()]
    queryset=Table.objects.all()
    serializer_class=TableGetSerializer

class TableDetail(RetrieveUpdateDestroyAPIView):
    throttle_classes=[GeneralThrottle]
    def get_permissions(self):
        if self.request.method=="GET":
            return [IsAuthenticated()]
        return [IsManager()]
    queryset=Table.objects.all()
    serializer_class=TableSerializer

class ReservationListAPI(ListAPIView):
    throttle_classes=[GeneralThrottle]
    permission_classes=[IsAuthenticated]
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer


class ReservationCreateAPI(APIView):
    throttle_classes=[GeneralThrottle]
    permission_classes=[IsCustomer]
    def post(self, request, pk):
        serial=ReservationSerializer(data=request.data)
        if serial.is_valid():
            table_data=get_object_or_404(Table, id=pk)
            if table_data.is_avaliable==True:
                serial.save(user=request.user, table=table_data)
                return Response(serial.data, status=201)
            return Response({'message':'table is already booked'}, status=400)
        return Response(serial.errors, status=400)

class ReservationDetailAPI(RetrieveDestroyAPIView):
    throttle_classes=[GeneralThrottle]
    def get_permissions(self):
        if self.request.method=="GET":
            return [IsAuthenticated()]
        return [IsCustomer()]
    serializer_class=ReservationSerializer
    queryset=Reservation.objects.all()
