from __future__ import unicode_literals

from django.db import models

# Create your models here.

class pet(models.Model):
    name = models.CharField(max_length = 40)
    health = models.IntegerField()
    experience = models.IntegerField()
    ownerIdNumber = models.IntegerField()
    typeIdNumber = models.IntegerField()
    age = models.DateTimeField()
