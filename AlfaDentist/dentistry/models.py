from django.db import models

# Create your models here.

class Query(models.Model):
    F_name=models.CharField(max_length=112)
    L_name=models.CharField(max_length=112)
    email=models.CharField(max_length=112)
    Phone=models.CharField(max_length=12)
    Query=models.TextField()
    Date=models.DateField()