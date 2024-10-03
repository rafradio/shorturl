from django.db import models

class Urlsshort(models.Model):
    link = models.CharField(max_length=250,)
    url = models.CharField(max_length=1250,)