  
from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100, null=True)
    emp_code = models.CharField(max_length=50, null=True)
    nature = models.CharField(max_length=100, null=True)
    mobile= models.CharField(max_length=15, null=True)
    email= models.CharField(max_length=40, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    position= models.ForeignKey(Position,on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname