# Generated by Django 3.1.14 on 2022-02-22 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20220217_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('M', 'Turno Matutino'), ('V', 'Turno Vespertino'), ('N', 'Turno Nocturno')], max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='shift',
            field=models.ManyToManyField(blank=True, null=True, to='employees.Shift'),
        ),
    ]