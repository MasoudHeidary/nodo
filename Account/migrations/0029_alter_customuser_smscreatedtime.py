# Generated by Django 3.2.6 on 2021-09-17 12:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0028_alter_customuser_smscreatedtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='SMSCreatedTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 17, 12, 54, 47, 338118, tzinfo=utc)),
        ),
    ]