# Generated by Django 3.1.14 on 2022-02-17 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file_employee', to='employees.employee')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='contract',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contract_file', to='employees.file'),
        ),
        migrations.AddField(
            model_name='employee',
            name='rfc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rfc_file', to='employees.file'),
        ),
    ]
