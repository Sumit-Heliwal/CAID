# Generated by Django 4.0.6 on 2024-04-10 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Data', '0003_remove_company_file_director_partner_list_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company_file',
            name='driving_licence',
        ),
        migrations.RemoveField(
            model_name='company_file',
            name='driving_licence_no',
        ),
    ]