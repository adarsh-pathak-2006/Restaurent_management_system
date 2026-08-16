from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Reservation, Table
from .serializers import TableGetSerializer, TableSerializer, ReservationSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class AllTables(ListCreateAPIView):
    queryset=Table.objects.all()
    serializer_class=TableGetSerializer

class TableDetail(RetrieveUpdateDestroyAPIView):
    queryset=Table.objects.all()
    serializer_class=TableSerializer

class ReservationListAPI(ListAPIView):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer


class ReservationCreateAPI(APIView):
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
    serializer_class=ReservationSerializer
    queryset=Reservation.objects.all()
