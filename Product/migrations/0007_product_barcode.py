# Generated by Django 3.2.6 on 2021-09-11 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0006_rename_category_productcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Barcode',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
    ]