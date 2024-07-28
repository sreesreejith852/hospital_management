from django.db import models
from customers.models import Customer
from products.models import Product

class Order(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES=((LIVE,'live'),(DELETE,'delete'))
    CART_STAGE = 1
    ORDERED_CONFIRMED = 1
    ORDERED_REJECTED = 4
    ORDER_PROCESSED = 2
    ORDER_DELIVERED = 3
    STATUS_CHOICE=((ORDER_PROCESSED, "ORDER_PROCESSED"),
                    (ORDER_DELIVERED,"ORDER_DELIVERED"),
                    (ORDERED_REJECTED, "ORDERED_REJECTED"))
    order_status = models.IntegerField(choices=STATUS_CHOICE, default=CART_STAGE)
    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL, null = True, related_name='orders')
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    cerated_at = models.DateTimeField(auto_now_add=True)
    updated_at =  models.DateTimeField(auto_now = True)


class OrderedItem(models.Model):
    product = models.ForeignKey(Product, related_name='added_cart', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(Order, on_delete=models.CASCADE,related_name='added_items')
