from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    quantity_in_stock = models.FloatField()
    price = models.FloatField()

    def __repr__(self):
        return self.name + ' is added.'

