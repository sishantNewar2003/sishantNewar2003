# Generated by Django 4.1.5 on 2023-04-26 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neona_sports', '0012_remove_order_customer_remove_order_order_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='payment_id',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
