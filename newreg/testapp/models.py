from django.db import models

# Create your models here.

class Student(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=64)
    esal=models.IntegerField()
    eaddr=models.CharField(max_length=64)