# Generated by Django 4.1.5 on 2023-01-20 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('RavantApp', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginDetails',
            fields=[
                ('user_id', models.IntegerField(db_column='User_ID', primary_key=True, serialize=False)),
                ('user_name', models.CharField(blank=True, db_column='User_name', max_length=45, null=True)),
                ('email_address', models.CharField(blank=True, db_column='Email_Address', max_length=45, null=True)),
                ('user_type', models.CharField(blank=True, db_column='User_Type', max_length=45, null=True)),
                ('password', models.CharField(db_column='Password', max_length=45)),
            ],
            options={
                'db_table': 'login_Details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MachinevisionCamera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_name', models.CharField(db_column='Machine_Name', max_length=45)),
                ('camera_id', models.CharField(blank=True, db_column='Camera_ID', max_length=45, null=True)),
                ('defect_image', models.CharField(blank=True, db_column='Defect_Image', max_length=45, null=True)),
                ('download_image', models.CharField(blank=True, db_column='Download_Image', max_length=45, null=True)),
                ('camera_status', models.CharField(blank=True, db_column='Camera_Status', max_length=45, null=True)),
            ],
            options={
                'db_table': 'MachineVision_Camera',
                'managed': False,
            },
        ),
    ]
