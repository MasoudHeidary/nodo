# Generated by Django 3.2.6 on 2021-09-16 07:33

import Product.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0010_product_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Image',
            field=models.ImageField(null=True, upload_to=Product.models.product_image_name),
        ),
        migrations.AlterField(
            model_name='product',
            name='Slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=150),
        ),
    ]