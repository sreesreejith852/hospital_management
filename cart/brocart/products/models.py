from django.db import models

class Product(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE, 'live'),(DELETE, 'Delete'))
    title = models.CharField(max_length=200)
    price = models.FloatField(max_length=100)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='images/')
    priority = models.IntegerField(default=0)
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    cerated_at = models.DateTimeField(auto_now_add=True)
    updated_at =  models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return self.title  