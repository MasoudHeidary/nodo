# Generated by Django 3.2.6 on 2021-09-02 20:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0012_alter_customuser_smscreatedtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='SMSCreatedTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 2, 20, 12, 1, 886239, tzinfo=utc)),
        ),
    ]
