# Generated by Django 4.0.6 on 2024-03-12 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company_file',
            fields=[
                ('code_no', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('pan_card', models.FileField(blank=True, null=True, upload_to='company_file')),
                ('udyam_aadhar', models.FileField(blank=True, null=True, upload_to='company_file')),
                ('gst', models.FileField(blank=True, null=True, upload_to='company_file')),
                ('incorporation_certificate', models.FileField(blank=True, null=True, upload_to='company_file')),
                ('partnership_deed', models.FileField(blank=True, null=True, upload_to='company_file')),
                ('tan', models.FileField(blank=True, null=True, upload_to='company_file')),
                ('Remarks', models.CharField(max_length=300)),
            ],
        ),
    ]