# Generated by Django 4.1.6 on 2023-02-27 15:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supplies', '0018_alter_purchase_dop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('total_coupons', models.PositiveIntegerField(default=0)),
                ('milk_coupons', models.PositiveIntegerField(default=0)),
                ('curd_coupons', models.PositiveIntegerField(default=0)),
                ('ton_coupons', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='MappedCoupons',
        ),
        migrations.AlterField(
            model_name='purchase',
            name='dop',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 27, 21, 3, 39, 194865)),
        ),
    ]
