from django.db import models

# Create your models here.
class Shift(models.Model):
    SHIP_CHOICES = [
        ('M', 'Turno Matutino'),
        ('V', 'Turno Vespertino'),
        ('N', 'Turno Nocturno'),
    ]

    name = models.CharField(max_length=50, blank=True, null=True, choices=SHIP_CHOICES)


class Employee(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    contract = models.ForeignKey(
        'File', related_name='contract_file', on_delete=models.CASCADE, null=True, blank=True
    )
    rfc = models.ForeignKey(
        'File', related_name='rfc_file', on_delete=models.CASCADE, null=True, blank=True
    )

    shift = models.ManyToManyField(Shift, blank=True)

    def __str__(self):
        return self.name

class File(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    employee = models.ForeignKey(
        'Employee', related_name='file_employee', on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.name

