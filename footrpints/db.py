# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Batches(models.Model):
    batchid = models.IntegerField(db_column='batchId', primary_key=True)  # Field name made lowercase.
    coursename = models.CharField(db_column='courseName', max_length=15, blank=True, null=True)  # Field name made lowercase.
    joinyear = models.TextField(db_column='joinYear', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    endyear = models.TextField(db_column='endYear', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'batches'


class OfficialAlumni(models.Model):
    regno = models.IntegerField(db_column='regNo', primary_key=True)  # Field name made lowercase.
    studentname = models.CharField(db_column='studentName', max_length=40)  # Field name made lowercase.
    mobile = models.CharField(max_length=15, blank=True, null=True)
    instmail = models.CharField(db_column='instMail', max_length=23, blank=True, null=True)  # Field name made lowercase.
    personalmail = models.CharField(db_column='personalMail', max_length=40, blank=True, null=True)  # Field name made lowercase.
    batchid = models.ForeignKey(Batches, models.DO_NOTHING, db_column='batchId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'official_alumni'
