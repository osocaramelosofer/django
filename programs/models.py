from django.db import models


# Creamos una relacion 1:M
# La foreign key va del lado del modelo en donde esta la M
# En este caso en ProgramRequirement
class Program(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    owner_name = models.CharField(max_length=50, null=True, blank=True)
    telephone = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class ProgramRequirement(models.Model):
    # el segundo elemento de la tupla sirve para mostrarse en el front
    TYPE_CHOICES = [
        ('PDF', 'DOCUMENTO TIPO PDF'),
        ('PNG', 'DOCUMENTO TIPO PNG'),
        ('JPG', 'DOCUMENTO TIPO JPG'),
    ]
    program = models.ForeignKey(
        'Program', related_name='program_requirement', on_delete=models.CASCADE, blank=True, null=True
    )
    name = models.CharField(max_length=50, null=True, blank=True)
    type = models.CharField(max_length=3, null=True, blank=True, choices=TYPE_CHOICES)

    def __str__(self):
        return self.name
