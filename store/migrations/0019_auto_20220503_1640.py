# Generated by Django 3.2.12 on 2022-05-03 11:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_auto_20220503_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 3, 16, 40, 55, 884832)),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 5, 3, 16, 40, 55, 884833)),
        ),
        migrations.AlterField(
            model_name='previous',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 3, 16, 40, 55, 885832)),
        ),
    ]
