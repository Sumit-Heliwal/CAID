# Generated by Django 4.0.6 on 2024-04-14 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personal_Data', '0004_alter_personal_file_din_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_file',
            name='din_no',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]