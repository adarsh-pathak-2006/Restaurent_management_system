from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Table, Reservation
from authentication.serializers import UserGetSerializer

class TableGetSerializer(ModelSerializer):
    class Meta:
        model=Table
        fields=['id', 'is_avaliable']

class TableSerializer(ModelSerializer):
    class Meta:
        model=Table
        fields='__all__'

class ReservationSerializer(ModelSerializer):
    user=UserGetSerializer(read_only=True)
    table=TableGetSerializer(read_only=True)
    # table=PrimaryKeyRelatedField(queryset=Table.objects.all())
    class Meta:
        model=Reservation
        fields='__all__'