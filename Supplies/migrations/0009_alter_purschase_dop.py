# Generated by Django 4.1.6 on 2023-02-15 06:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supplies', '0008_alter_purschase_coupons_alter_purschase_dop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purschase',
            name='dop',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 15, 12, 15, 25, 999683)),
        ),
    ]
