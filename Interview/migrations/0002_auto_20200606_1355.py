# Generated by Django 3.0.7 on 2020-06-06 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Interview', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interview',
            old_name='data',
            new_name='date',
        ),
    ]