from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=40)
    branch=models.CharField(max_length=50)
    sid=models.IntegerField()
    email=models.EmailField()
    doj=models.DateField()