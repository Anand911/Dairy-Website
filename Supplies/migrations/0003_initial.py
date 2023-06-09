# Generated by Django 4.1.6 on 2023-02-14 08:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Supplies', '0002_delete_customer_delete_purschase_delete_supplier'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.CharField(max_length=20)),
                ('c_fname', models.CharField(max_length=20)),
                ('c_lname', models.CharField(max_length=20)),
                ('phone', models.PositiveBigIntegerField()),
                ('address', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Purschase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_id', models.CharField(max_length=10, unique=True)),
                ('dop', models.DateTimeField(default=datetime.datetime(2023, 2, 14, 14, 16, 44, 313793))),
                ('total_purchase', models.BigIntegerField(default=0)),
                ('availed_coupons', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('coupons', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_fname', models.CharField(max_length=20)),
                ('s_lname', models.CharField(max_length=20)),
                ('phone', models.PositiveBigIntegerField()),
                ('Adhaar_no', models.PositiveBigIntegerField(null=True)),
                ('supply_area', models.CharField(choices=[('Ramamurthy Nagar', 'Ramamurthy Nagar'), ('Hormavu', 'Hormavu'), ('Banasawadi', 'Banaswadi')], max_length=20)),
            ],
        ),
    ]
