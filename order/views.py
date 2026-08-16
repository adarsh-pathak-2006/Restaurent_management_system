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
    def get_queryset(self):
        if self.request.user.role == 'MANAGER':
            return Order.objects.all()
        return Order.objects.filter(table__reservation__user=self.request.user)

class OrderCreateAPI(APIView):
    throttle_classes=[GeneralThrottle]
    permission_classes=[IsCustomer]
    def post(self, request, pk, ck):
        serial=OrderSerializer(data=request.data)
        if serial.is_valid():
            table_data=get_object_or_404(Table, id=pk)
            if not hasattr(table_data, 'reservation') or table_data.reservation.user != request.user:
                return Response({'message':'Table is not reserved by you'}, status=403)
            
            menu_data=get_object_or_404(Menu, id=ck)
            quantity = serial.validated_data.get('item_quantity', 1)
            
            if menu_data.stock < quantity or not menu_data.is_avaliable:
                return Response({'message':'Not enough stock available'}, status=400)
                
            serial.save(items=menu_data, table=table_data)
            menu_data.stock = menu_data.stock - quantity
            menu_data.save()
            return Response(serial.data, status=201)
        return Response(serial.errors, status=400)

class OrderDetailAPI(RetrieveUpdateDestroyAPIView):
    throttle_classes=[GeneralThrottle]
    def get_permissions(self):
        if self.request.method=='GET':
            return [IsAuthenticated()]
        return [IsCustomer()]
    serializer_class=OrderGetSerializer
    def get_queryset(self):
        if self.request.user.role == 'MANAGER':
            return Order.objects.all()
        return Order.objects.filter(table__reservation__user=self.request.user)


