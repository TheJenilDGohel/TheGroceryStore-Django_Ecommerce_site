# Generated by Django 4.0.5 on 2022-06-08 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_cart_item_timestamp_cart_item_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart_item',
            name='product',
        ),
        migrations.DeleteModel(
            name='cart',
        ),
        migrations.DeleteModel(
            name='cart_item',
        ),
    ]