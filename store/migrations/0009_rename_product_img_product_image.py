# Generated by Django 4.0.5 on 2022-06-06 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_product_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_img',
            new_name='image',
        ),
    ]
