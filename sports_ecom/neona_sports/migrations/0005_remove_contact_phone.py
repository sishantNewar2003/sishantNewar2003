# Generated by Django 4.1.5 on 2023-03-18 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neona_sports', '0004_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
    ]
