# Generated by Django 2.1.5 on 2019-08-28 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_auto_20190828_0845'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='user',
            new_name='owner',
        ),
    ]
