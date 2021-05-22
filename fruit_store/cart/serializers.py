from rest_framework import serializers
from .models import Cart, CartItem

class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ('product', 'quantity')

class CartItemListingField(serializers.RelatedField):
    def to_representation(self, value):
        return {value.product.name: value.quantity}

class CartSerializer(serializers.ModelSerializer):

    customer = serializers.StringRelatedField(many=False)

    cart_items = CartItemListingField(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Cart
        fields = ('customer', 'cart_items')