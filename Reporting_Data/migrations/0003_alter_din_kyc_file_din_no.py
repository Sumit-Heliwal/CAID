# Generated by Django 4.0.6 on 2024-04-15 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reporting_Data', '0002_alter_din_kyc_file_din_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='din_kyc_file',
            name='din_no',
            field=models.IntegerField(max_length=50, unique=True),
        ),
    ]
