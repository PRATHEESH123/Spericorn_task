from django.db import models


# Create your models here.



class Members(models.Model):
    """Model defnition for Members."""

    Member = 0
    Coach = 1
    Manager = 2

    CATEGORY_CHOICES = (
        (Member, 'Member'),
        (Coach, 'Coach'),
        (Manager, 'Manager'),
    )

    team = models.ForeignKey('Team_Name', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
    date_of_birth= models.CharField(max_length=50)
    contact_detail = models.TextField(max_length=100)

    def __str__(self):
        """Unicode representation of Members."""
        return f'{self.team}'