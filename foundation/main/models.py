from django.db import models

# Create your models here.
class Char(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)