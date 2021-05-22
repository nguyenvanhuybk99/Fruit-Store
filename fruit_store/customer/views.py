import ast
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import *
from shop.models import Product
from customer.models import Customer, Order, OrderItem
from cart.models import Cart, CartItem

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        data = {
            'username': request.data.get('username'),
            'hash_password' : str(hash(request.data.get('password')))
        }
        serializer = CustomerSerializer(data = data)

        if serializer.is_valid():
            serializer.save()      
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def place_order(request):
    if request.method == 'POST':
        # check product is available in stock
        customer = Customer.objects.filter(username = request.data.get('username'))[0]
        try:
            cart = Cart.objects.get(pk = customer.id)
        except Cart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        cart_items = cart.cart_items.all()
        items = dict([[item.product.name, item.quantity] for item in cart_items])

        if sum(items.values()) == 0:
            return Response({"request status":"Cart is empty, nothing to order"}, status=status.HTTP_400_BAD_REQUEST)

        for name, quantity in items.items():
            product = Product.objects.filter(name=name)[0]
            # if not enough quantity
            if product.quantity_in_stock < quantity:
                return Response({"request status":"Canceled, not enough " + product.name}, status=status.HTTP_400_BAD_REQUEST)

        # create order      
        data = {
            'customer': customer,
            'status': 'Processing'
        }
        order = Order.objects.create(**data)

        # add item to order and update shop
        for name, quantity in items.items():
            product = Product.objects.filter(name=name)[0]

            # create order item
            OrderItem.objects.create(
                product = product,
                quantity = quantity, 
                price = product.price,
                order = order
            )

            # update product quantity in stock
            product.quantity_in_stock -= quantity
            product.save()

        # empty cart
        for cart_item in cart_items:
            cart_item.delete()
        Cart.objects.get(pk = customer.id).delete()

        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_order_detail(request, pk):
    if request.method == 'GET':
        customer = Customer.objects.filter(username = request.data.get('username'))[0]
        try:          
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if order.customer == customer:
            return Response(OrderSerializer(order).data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_order_list(request):
    if request.method == 'GET':
        customer = Customer.objects.filter(username = request.data.get('username'))[0]        
        orders = Order.objects.filter(customer = customer)

        serializer = OrderListSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
