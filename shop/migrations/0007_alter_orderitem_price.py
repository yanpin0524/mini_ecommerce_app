# Generated by Django 4.2.13 on 2024-05-09 04:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_cartitem_quantity_alter_orderitem_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
    ]
