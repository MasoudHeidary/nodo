# Generated by Django 3.2.6 on 2021-09-28 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0016_alter_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='subproduct',
            name='BriefDescription',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]