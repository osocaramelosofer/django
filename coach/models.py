from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Coach(models.Model):
    SHIFT_CHOICES = [
        ('D', 'Day'),
        ('N', 'Night'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shift = models.CharField(max_length=1, choices=SHIFT_CHOICES)

    def __str__(self):
        return f"{self.user.username}"