# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-08 12:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(help_text='Put Contact Name Here, Do not put business name', max_length=50, verbose_name='Contact Name')),
                ('contact_number', models.IntegerField(help_text='Put 8 digit Singapore Number', max_length=6, verbose_name='Contact Number')),
                ('contact_email', models.EmailField(max_length=254, verbose_name='Contact Email')),
                ('company_name', models.CharField(help_text='Business Trading Name', max_length=75, verbose_name='Company Name')),
                ('company_reg_no', models.CharField(max_length=10, verbose_name='Company Registration Number')),
            ],
        ),
        migrations.CreateModel(
            name='Shipping_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_address_line1', models.CharField(max_length=75, verbose_name='Block Number and Street Name')),
                ('shipping_address_line2', models.CharField(max_length=75, verbose_name='Unit Number and Building Name')),
                ('shipping_postal', models.IntegerField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Billing_Details',
            fields=[
                ('customer_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='customers.Customer')),
                ('billing_address_line1', models.CharField(max_length=75, verbose_name='Block Number and Street Name')),
                ('billing_address_line2', models.CharField(max_length=75, verbose_name='Unit Number and Building Name')),
                ('billing_postal', models.IntegerField(max_length=6)),
            ],
        ),
        migrations.AddField(
            model_name='shipping_details',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Customer'),
        ),
    ]
