# Generated by Django 4.1.6 on 2023-02-23 09:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supplies', '0014_purchase_delete_purschase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='dop',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 23, 14, 47, 3, 972163)),
        ),
    ]
