from django.db import models

class quickstart(models.Model):
    name = models.CharField(max_length=50)
    paradiga = models.CharField(max_length=50)
    