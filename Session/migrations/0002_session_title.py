# Generated by Django 3.0.7 on 2020-06-06 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Session', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='title',
            field=models.CharField(default='', max_length=500),
        ),
    ]
