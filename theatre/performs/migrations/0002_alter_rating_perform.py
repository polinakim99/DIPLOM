# Generated by Django 3.2.9 on 2022-04-22 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('performs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='perform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='performs.perform', verbose_name='спектакль'),
        ),
    ]
