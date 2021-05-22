from django.db import models
from shop.models import Product
from customer.models import Customer

class Cart(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField() 
 
