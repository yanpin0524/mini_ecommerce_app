# Generated by Django 4.2.13 on 2024-05-20 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_remove_orderitem_price_order_order_no_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment_status',
        ),
    ]