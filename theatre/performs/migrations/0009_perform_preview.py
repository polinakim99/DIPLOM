# Generated by Django 3.2.9 on 2022-05-15 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performs', '0008_rename_performshorts_performshots'),
    ]

    operations = [
        migrations.AddField(
            model_name='perform',
            name='preview',
            field=models.ImageField(default='sdsd', upload_to='perform/', verbose_name='Превью'),
        ),
    ]
