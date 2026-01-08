from django.db import models


class profile(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class marks(models.Model):
    stu_sub = models.CharField(max_length=50)
    marks = models.IntegerField()


class group(models.Model):
    group_name = models.CharField(max_length=100)
    group_rank = models.CharField(max_length=100)
