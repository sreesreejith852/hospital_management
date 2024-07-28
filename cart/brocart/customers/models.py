from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES=((LIVE,'live'),(DELETE,'delete'))
    name = models.CharField(max_length=150)
    address =   models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='customer_profile')
    phone =  models.CharField(max_length=10)
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    cerated_at = models.DateTimeField(auto_now_add=True)
    updated_at =  models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return self.name