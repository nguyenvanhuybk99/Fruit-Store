from django.db import models
from shop.models import Product

STATUS_CHOICES = (
    ('Processing', 'Processing'), 
    ('Shipped', 'Shipped'),
    ('Complete', 'Complete'),
    ('Canceled', 'Canceled'), 
)

class Customer(models.Model):
    username = models.CharField(max_length=255, unique=True)
    hash_password = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='order_list', on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES, default='Processing',max_length = 30)
    created_at = models.DateTimeField(auto_now_add = True) 

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.FloatField()
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
