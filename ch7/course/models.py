from django.db import models


class info(models.Model):
    name = models.CharField(max_length=70)
    date = models.DateField()
    price = models.IntegerField()
    place_of_origin = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, default="abinaya13@gmail.com")
