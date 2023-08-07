from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    idNo = models.IntegerField()
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    salary = models.FloatField()
