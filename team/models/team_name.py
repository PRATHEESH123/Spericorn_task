from django.db import models

# Create your models here.


class Team_Name(models.Model):
    """Model defnition for Team_Name."""

    name = models.CharField(max_length=50)
    score = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        """Unicode representation of Team_Name."""
        return f'{self.name}'