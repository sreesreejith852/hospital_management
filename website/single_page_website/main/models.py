from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    mobile = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()




class Task(models.Model):
    name = models.CharField(max_length=150)
    datetime = models.DateTimeField()
    assigned_to = models.ForeignKey(
        User,
        related_name='assigned_tasks',  # Unique related name for tasks assigned to this user
        on_delete=models.CASCADE
    )
    created_by = models.ForeignKey(
        User,
        related_name='created_tasks',  # Unique related name for tasks created by this user
        on_delete=models.CASCADE
    )
    status = models.CharField(max_length=50, default='Pending')
