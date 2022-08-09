from django.db import models

# Create your models here.
class student(models.Model):
    Student_name=models.CharField(max_length=200)
    Student_Regno=models.IntegerField(max_length=100)
    Address=models.CharField(max_length=1000)
    College_name=models.CharField(max_length=100)
    Course=models.CharField(max_length=100)