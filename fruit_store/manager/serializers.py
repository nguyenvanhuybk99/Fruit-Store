from rest_framework import serializers
from shop.models import Product

class ManagerProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'quantity_in_stock')