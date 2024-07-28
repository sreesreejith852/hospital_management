from django.db import models

# Create your models here.

class CensiorINFO(models.Model):
    rating = models.CharField(max_length=100, null=True)
    certified_by = models. CharField(max_length=100, null=True)
 
class MovieInfo(models.Model):
    title = models.CharField(max_length=250)
    year = models.IntegerField(null=True)
    summary = models.TextField()
    censior_details = models.OneToOneField(CensiorINFO, on_delete=models.SET_NULL, related_name='movie', null=True)

class Director(models.Model):
    name = models.CharField(max_length=100)

class Actors(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField(max_length=10)


 