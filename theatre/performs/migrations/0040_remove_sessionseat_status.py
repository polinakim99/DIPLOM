# Generated by Django 2.2.28 on 2022-06-07 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('performs', '0039_auto_20220607_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sessionseat',
            name='status',
        ),
    ]
