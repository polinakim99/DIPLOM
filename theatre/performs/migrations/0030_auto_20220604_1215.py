# Generated by Django 2.2.28 on 2022-06-04 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('performs', '0029_auto_20220604_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seans',
            name='perform',
        ),
        migrations.DeleteModel(
            name='Bron',
        ),
        migrations.DeleteModel(
            name='Seans',
        ),
    ]
