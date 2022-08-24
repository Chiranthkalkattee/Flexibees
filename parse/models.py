from django.db import models

# Create your models here.
class Employee_details(models.Model):
    Employee_name = models.CharField(max_length=100)
    Phone_number = models.IntegerField()
    Email = models.EmailField(max_length=300)
    Designation = models.CharField(max_length=50)