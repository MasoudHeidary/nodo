# Generated by Django 3.2.6 on 2021-09-16 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0009_subproduct_sellonline'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Active',
            field=models.BooleanField(default=False),
        ),
    ]
