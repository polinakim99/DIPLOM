# Generated by Django 2.2.28 on 2022-06-07 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('performs', '0030_auto_20220604_1215'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rating',
        ),
        migrations.DeleteModel(
            name='RatingStar',
        ),
    ]
