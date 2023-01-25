from django.db import models
from django.contrib import auth

class LoginDetails(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=45, blank=True, null=True)
    email_address = models.CharField(max_length=45, blank=True, null=True)
    user_type = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'login_Details'

class MachinevisionCamera(models.Model):
    machine_id = models.AutoField(primary_key=True)
    machine_name = models.CharField(max_length=45, blank=True, null=True)
    camera_id = models.IntegerField(blank=True, null=True)
    defect_image = models.CharField(max_length=45, blank=True, null=True)
    download_image = models.CharField(max_length=45, blank=True, null=True)
    camera_status = models.CharField(max_length=45, blank=True, null=True)
    user = models.ForeignKey('LoginDetails', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MachineVision_Camera'