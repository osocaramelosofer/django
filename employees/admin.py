from django.contrib import admin
from .models import Employee, File, Shift


# Register your models here.
admin.site.register(Employee)
admin.site.register(File)
admin.site.register(Shift)

