from rest_framework import serializers
from .models import Customer, Order, OrderItem

# Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('username', 'hash_password')

# Order and OrderItem 

class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ('product', 'quantity', 'price')

class OrderItemListingField(serializers.RelatedField):
    def to_representation(self, value):
        return {"name": value.product.name, 'quantity':value.quantity, 'price':value.price}
            

class OrderSerializer(serializers.ModelSerializer):

    customer = serializers.StringRelatedField(many=False)

    order_items = OrderItemListingField(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Order
        fields = ('id', 'customer', 'status', 'created_at', 'order_items')


class OrderListSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField(many=False)

    class Meta:
        model = Order
        fields = ('id', 'customer', 'status')