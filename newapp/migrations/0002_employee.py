# Generated by Django 5.1 on 2024-08-27 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE'), ('O', 'OTHER')], max_length=10)),
                ('address', models.CharField(max_length=20)),
                ('salary', models.IntegerField()),
                ('department', models.CharField(choices=[('FD', 'FRONTEND'), ('BD', 'BACKEND'), ('DD', 'DATABASE')], max_length=10)),
                ('working_hrs', models.DateTimeField(auto_now_add=True)),
                ('shift', models.CharField(max_length=10)),
            ],
        ),
    ]
