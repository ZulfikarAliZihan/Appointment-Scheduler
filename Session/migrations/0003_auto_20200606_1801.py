# Generated by Django 3.0.7 on 2020-06-06 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Session', '0002_session_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='session',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
