# Generated by Django 4.1.6 on 2023-02-17 08:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Supplies', '0011_alter_purschase_coupons_alter_purschase_dop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purschase',
            name='dop',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 17, 13, 49, 32, 699746)),
        ),
        migrations.AlterField(
            model_name='purschase',
            name='purchase_customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='Supplies.customer'),
        ),
    ]
