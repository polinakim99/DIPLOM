# Generated by Django 3.2.9 on 2022-05-27 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performs', '0012_auto_20220527_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perform',
            name='categories',
            field=models.ManyToManyField(default='жбр', to='performs.Category', verbose_name='категории'),
        ),
    ]
