# Generated by Django 4.0.5 on 2022-08-06 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0026_remove_order_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
