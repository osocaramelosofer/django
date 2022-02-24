# Generated by Django 3.1.14 on 2022-02-21 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('owner_name', models.CharField(blank=True, max_length=50, null=True)),
                ('telephone', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProgramRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('type', models.CharField(blank=True, choices=[('PDF', 'DOCUMENTO TIPO PDF'), ('PNG', 'DOCUMENTO TIPO PNG'), ('JPG', 'DOCUMENTO TIPO JPG')], max_length=3, null=True)),
                ('program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='program_requirement', to='programs.program')),
            ],
        ),
    ]