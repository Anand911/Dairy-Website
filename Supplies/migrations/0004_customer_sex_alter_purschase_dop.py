# Generated by Django 4.1.6 on 2023-02-14 08:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supplies', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='sex',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='purschase',
            name='dop',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 14, 14, 28, 24, 212220)),
        ),
    ]
