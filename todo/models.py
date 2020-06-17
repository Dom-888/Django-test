from django.db import models

# Create your models here.

class Item(models.model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BolleanField(null=False, blank=False, default=False)