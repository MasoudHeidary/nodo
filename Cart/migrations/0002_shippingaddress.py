# Generated by Django 3.2.6 on 2021-09-20 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('State', models.CharField(max_length=30)),
                ('City', models.CharField(max_length=30)),
                ('Address', models.CharField(max_length=250)),
                ('HouseNumber', models.CharField(max_length=5)),
                ('FloorNumber', models.CharField(max_length=3)),
                ('ZipCode', models.CharField(max_length=10)),
                ('ToCart', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Cart.cart')),
            ],
        ),
    ]
