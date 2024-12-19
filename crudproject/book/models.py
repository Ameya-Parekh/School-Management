from django.db import models
# Create your models here.

class User(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=20)
    Password=models.CharField(max_length=50)

