from django.db import models

# Create your models here.
class users(models.Model):
    email=models.EmailField(max_length=20)
    name=models.CharField(max_length=50)

class person(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)