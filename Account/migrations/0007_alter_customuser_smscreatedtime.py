# Generated by Django 3.2.6 on 2021-08-30 17:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0006_alter_customuser_smscreatedtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='SMSCreatedTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 30, 17, 17, 36, 15161, tzinfo=utc)),
        ),
    ]
