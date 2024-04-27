from django.db import models

# Create your models here.
class Retailer(models.Model):
    name = models.CharField(max_length=255)
