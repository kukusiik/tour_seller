from django.db import models

class TourOperator(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)