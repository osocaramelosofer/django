from django.db import models
from django.urls import reverse # new


# Create your models here.
class Gym(models.Model):
    # pk
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    capacity = models.IntegerField()

    def __str__(self):
        return f"Gym Name = {self.name}"

    def get_absolute_url(self): # new
        return reverse('gym_detail', args=[str(self.id)])

