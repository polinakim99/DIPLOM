# Generated by Django 3.2.9 on 2022-05-30 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('performs', '0016_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='user',
            new_name='username',
        ),
    ]
