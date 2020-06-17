from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self): # Overwrite the string method so that it returns the name of the element
        return self.name