# Generated by Django 4.1.5 on 2023-02-17 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neona_sports', '0002_auto_20230215_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Availibilty',
            field=models.CharField(choices=[('In Stock', 'In Stock'), ('Out of Stock', 'Out of Stock')], max_length=100, null=True),
        ),
    ]
