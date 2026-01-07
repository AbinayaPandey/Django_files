from django.db import models


class profile(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=150)
