# Generated by Django 3.2.6 on 2021-09-20 07:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0033_alter_customuser_smscreatedtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='SMSCreatedTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 20, 7, 34, 8, 582928, tzinfo=utc)),
        ),
    ]
