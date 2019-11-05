from django.db import models

# Create your models here.
class product (models.Model):
    pid= models.CharField(max_length=10)
    pname= models.CharField(max_length=100)
    des=models.CharField(max_length=500)
    price=models.CharField(max_length=500)
    price= models.IntegerField()
    features =models.CharField(max_length=500)
    mdate= models.DateField()