# Generated by Django 3.2.6 on 2021-09-16 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0012_alter_product_tocategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=100),
        ),
    ]
