from rest_framework.serializers import ModelSerializer
from .models import Table, Reservation
from authentication.serializers import UserGetSerializer

class TableGetSerializer(ModelSerializer):
    class Meta:
        model=Table
        fields=['table_id', 'is_avaliable']

class TableSerializer(ModelSerializer):
    class Meta:
        model=Table
        fields='__all__'

class ReservationSerializer(ModelSerializer):
    user=UserGetSerializer(read_only=True)
    class Meta:
        model=Reservation
        fields='__all__'