from django.db import models

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=100)
    email = models.EmailField(max_length=100)
