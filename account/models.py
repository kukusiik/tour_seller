from django.db import models

# Create your models here.
class account(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)