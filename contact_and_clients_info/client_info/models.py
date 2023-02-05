from django.db import models


class Client(models.Model):
    fullName = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    entry = models.CharField(max_length=11)
