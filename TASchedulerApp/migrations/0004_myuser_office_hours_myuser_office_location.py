# Generated by Django 5.1.3 on 2024-12-12 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TASchedulerApp', '0003_myuser_home_address_myuser_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='office_hours',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='myuser',
            name='office_location',
            field=models.CharField(default='', max_length=50),
        ),
    ]
