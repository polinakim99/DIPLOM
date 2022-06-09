# Generated by Django 3.2.9 on 2022-05-30 01:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('performs', '0019_alter_reviews_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='username',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
