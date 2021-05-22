import ast
from shop.models import Product
from customer.models import Customer, Order, OrderItem
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

@api_view(['GET'])
def cart(request):
    if request.method == 'GET':

        customer = Customer.objects.filter(username = request.data.get('username'))[0]
        try:
            cart = Cart.objects.get(pk = customer.id)    
        except Cart.DoesNotExist:
            return Response({"request status: ":"cart is empty!"}, status=status.HTTP_404_NOT_FOUND) 

        return Response(CartSerializer(cart).data)

@api_view(['PUT'])
def add_to_cart(request, pk):
    if request.method == 'PUT':
        # get product and check status in stock
        product = Product.objects.get(pk=pk)
        if product.quantity_in_stock == 0:
            return Response({"request status: ":product.name + " is out of stock"}, status=status.HTTP_400_BAD_REQUEST)

        # get cart / create new cart
        customer = Customer.objects.filter(username = request.data.get('username'))[0]  
        if len(Cart.objects.filter(customer = customer)) > 0:
            cart = Cart.objects.filter(customer = customer)[0]
        else:
            data = {'customer': customer} 
            cart = Cart.objects.create(**data)
        
        if len(CartItem.objects.filter(cart = cart, product = product)) > 0:
            cart_item = CartItem.objects.filter(cart = cart, product = product)[0]
            if cart_item.quantity  < product.quantity_in_stock :
                cart_item.quantity += 1
                cart_item.save()
            else:
                return Response({"status request: ":"not enough product"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            CartItem.objects.create(
                cart = cart,
                product = product,
                quantity = 1
            )

        return Response(CartSerializer(cart).data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def update_cart(request, pk):
    if request.method == 'PUT':
        # check product quantity in stock
        products_request = ast.literal_eval(request.data.get('fruits'))
        for name, quantity in products_request.items():
            product = Product.objects.filter(name=name)[0]
            if product.quantity_in_stock < quantity:
                return Response({"status request: ":"not enough product"}, status=status.HTTP_400_BAD_REQUEST)

        # get cart / create new cart
        cart = Cart.objects.get(pk = pk)
        cart_items = cart.cart_items.all()

        for item in cart_items:
            if item.product.name not in products_request:
                continue
            if products_request[item.product.name] == 0:
                item.delete()
            else:
                item.quantity = products_request[item.product.name]
                item.save()


        return Response(CartSerializer(cart).data, status=status.HTTP_201_CREATED)
