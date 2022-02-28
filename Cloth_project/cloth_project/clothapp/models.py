from distutils.command.upload import upload
from django.db import models
from django.forms import FloatField

# Create your models here.

class Cloth(models.Model):
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    img = models.ImageField(upload_to='images')
    des = models.TextField()
    price = models.FloatField(max_length=100)

    def __str__(self):
        return self.name