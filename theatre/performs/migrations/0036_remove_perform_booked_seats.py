# Generated by Django 2.2.28 on 2022-06-07 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('performs', '0035_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perform',
            name='booked_seats',
        ),
    ]