# Generated by Django 2.2.28 on 2022-06-07 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performs', '0033_session_sessionseat'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessionseat',
            name='booked',
            field=models.BooleanField(default=False, verbose_name='Занято'),
        ),
    ]