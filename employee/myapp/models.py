from django.db import models

class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    mobile = models.IntegerField()
    password = models.CharField(max_length=20)
