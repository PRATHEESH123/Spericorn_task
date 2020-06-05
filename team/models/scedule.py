#django
from django.db import models

#thirdparty
from datetime import datetime


# Create your models here.



class Scedule(models.Model):
    """Model defnition for Scedule."""

    date = models.DateTimeField()
    venue = models.CharField(max_length=50)
    result= models.CharField(max_length=50)

    def __str__(self):
        """Unicode representation of Members."""
        return f'{self.date}'