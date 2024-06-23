# Generated by Django 4.0.6 on 2024-04-16 17:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reporting_Data', '0003_alter_din_kyc_file_din_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='din_kyc_file',
            name='KYC_date',
            field=models.DateField(default=datetime.date(2024, 4, 16)),
        ),
        migrations.AlterField(
            model_name='din_kyc_file',
            name='din_no',
            field=models.IntegerField(unique=True),
        ),
    ]
