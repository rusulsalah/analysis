# Generated by Django 3.1.2 on 2020-11-09 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csvs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='csv',
            old_name='activate',
            new_name='activated',
        ),
        migrations.RenameField(
            model_name='csv',
            old_name='upload',
            new_name='uploaded',
        ),
    ]
