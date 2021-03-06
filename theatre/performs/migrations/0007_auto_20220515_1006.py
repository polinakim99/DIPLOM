# Generated by Django 3.2.9 on 2022-05-15 00:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('performs', '0006_auto_20220502_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='perform',
            name='pushkin',
            field=models.BooleanField(default=False, verbose_name='Пушкинская карта'),
        ),
        migrations.AlterField(
            model_name='perform',
            name='date1',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Выступление_1'),
        ),
        migrations.AlterField(
            model_name='perform',
            name='date2',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Выступление_2'),
        ),
        migrations.AlterField(
            model_name='perform',
            name='date3',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Выступление_3'),
        ),
    ]
