# Generated by Django 4.0.6 on 2024-03-15 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Personal_Data', '0002_personal_file_ptec_personal_file_ptec_no_and_more'),
        ('Company_Data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_file',
            name='PTEC',
            field=models.FileField(blank=True, null=True, upload_to='company_file'),
        ),
        migrations.AddField(
            model_name='company_file',
            name='PTEC_no',
            field=models.CharField(default='Asia/Kolkata', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company_file',
            name='PTRC',
            field=models.FileField(blank=True, null=True, upload_to='company_file'),
        ),
        migrations.AddField(
            model_name='company_file',
            name='PTRC_no',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company_file',
            name='din',
            field=models.FileField(blank=True, null=True, upload_to='company_file'),
        ),
        migrations.AddField(
            model_name='company_file',
            name='din_no',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company_file',
            name='director_partner_list',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Personal_Data.personal_file'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company_file',
            name='driving_licence',
            field=models.FileField(blank=True, null=True, upload_to='company_file'),
        ),
        migrations.AddField(
            model_name='company_file',
            name='driving_licence_no',
            field=models.CharField(default=11, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company_file',
            name='gst_no',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company_file',
            name='name',
            field=models.CharField(default=11, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company_file',
            name='pan_no',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company_file',
            name='tan_no',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company_file',
            name='udyam_aadhar_no',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
