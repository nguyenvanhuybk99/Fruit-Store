from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from shop.models import Product
from .serializers import ManagerProductSerializer
from customer.models import Customer, Order, OrderItem
from customer.serializers import CustomerSerializer, OrderSerializer, OrderItemSerializer
from customer.serializers import OrderSerializer, OrderListSerializer


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single product
    if request.method == 'GET':
        serializer = ManagerProductSerializer(product)

        return Response(serializer.data)

    # delete a single product
    elif request.method == 'DELETE':
        product.delete()
        data = {
            "request status": "success"
        }
        return Response(data, status=status.HTTP_200_OK)

    # update details of a single product
    elif request.method == 'PUT':
        serializer = ManagerProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_product(request):
    # get all product
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ManagerProductSerializer(products, many=True)
        return Response(serializer.data)

    # insert a new record for a product
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'price': float(request.data.get('price')),
            'quantity_in_stock': float(request.data.get('quantity'))
        }

        # if product is already in shop, then update product
        if len(Product.objects.filter(name=data['name'])) > 0:
            product = Product.objects.filter(name=data['name'])[0]
            data['quantity_in_stock'] += product.quantity_in_stock

            serializer = ManagerProductSerializer(product, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        # product is not available in shop
        else:
            serializer = ManagerProductSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_customer(request):
    # get all customer
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_order_detail(request, pk):
    if request.method == 'GET':
        try:          
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(OrderSerializer(order).data, status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def get_order_list(request):
    if request.method == 'GET':   
        orders = Order.objects.all()
        serializer = OrderListSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)