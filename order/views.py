from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from order.models import Menu, Order
from order.serializers import MenuSerializer, MenuGetSerializer, OrderGetSerializer, OrderSerializer
from booking.models import Table
from config.throttling import GeneralThrottle
from config.permissions import IsCustomer, IsManager
from rest_framework.permissions import IsAuthenticated


class MenuAPI(ListCreateAPIView):
    throttle_classes=[GeneralThrottle]
    def get_permissions(self):
        if self.request.method=='GET':
            return [IsAuthenticated()]
        return [IsManager()]
    def get_serializer_class(self):
        if self.request.method=='GET':
            return MenuGetSerializer
        return MenuSerializer
    queryset=Menu.objects.all()       

class MenuRetrieveAPI(RetrieveUpdateDestroyAPIView):
    throttle_classes=[GeneralThrottle]
    def get_permissions(self):
        if self.request.method=='GET':
            return [IsAuthenticated()]
        return [IsManager()]
    def get_serializer_class(self):
        if self.request.method=='GET':
            return MenuGetSerializer
        return MenuSerializer
    queryset=Menu.objects.all()

class OrderAPI(ListAPIView):
    throttle_classes=[GeneralThrottle]
    permission_classes=[IsAuthenticated]
    serializer_class=OrderGetSerializer
    queryset=Order.objects.all()

class OrderCreateAPI(APIView):
    throttle_classes=[GeneralThrottle]
    permission_classes=[IsCustomer]
    def post(self, request, pk, ck):
        serial=OrderSerializer(data=request.data)
        if serial.is_valid():
            table_data=get_object_or_404(Table, id=pk)
            menu_data=get_object_or_404(Menu, id=ck)
            serial.save(items=menu_data, table=table_data)
            return Response(serial.data, status=201)
        return Response(serial.errors, status=400)

class OrderDetailAPI(RetrieveUpdateDestroyAPIView):
    throttle_classes=[GeneralThrottle]
    def get_permissions(self):
        if self.request.method=='GET':
            return [IsAuthenticated()]
        return [IsCustomer()]
    serializer_class=OrderGetSerializer
    queryset=Order.objects.all()


