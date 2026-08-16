from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Menu, Order
from booking.models import Table
from booking.serializers import TableGetSerializer

class MenuGetSerializer(ModelSerializer):
    class Meta:
        model=Menu
        fields=['id', 'item_name', 'item_price', 'is_avaliable']

class MenuSerializer(ModelSerializer):
    class Meta:
        model=Menu
        fields='__all__'

class OrderGetSerializer(ModelSerializer):
    items=MenuGetSerializer(read_only=True)
    table=TableGetSerializer(read_only=True)
    class Meta:
        model=Order
        fields='__all__'

class OrderSerializer(ModelSerializer):
    items=PrimaryKeyRelatedField(queryset=Menu.objects.all())
    table=PrimaryKeyRelatedField(queryset=Table.objects.all())
    class Meta:
        model=Order
        fields='__all__'