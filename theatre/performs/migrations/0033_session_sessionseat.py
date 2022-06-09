# Generated by Django 2.2.28 on 2022-06-07 14:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('performs', '0032_remove_seat_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Выступление_1')),
                ('perform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='performs.Perform', verbose_name='Спектакль')),
            ],
            options={
                'verbose_name': 'Сеанс',
                'verbose_name_plural': 'Сеансы',
            },
        ),
        migrations.CreateModel(
            name='SessionSeat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='performs.Seat', verbose_name='Место')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='performs.Session', verbose_name='Сеанс')),
            ],
            options={
                'verbose_name': 'Распределение мест',
                'verbose_name_plural': 'Распределения мест',
            },
        ),
    ]
