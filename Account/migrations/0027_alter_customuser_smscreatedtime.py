# Generated by Django 3.2.6 on 2021-09-16 07:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0026_alter_customuser_smscreatedtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='SMSCreatedTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 7, 36, 18, 15731, tzinfo=utc)),
        ),
    ]
