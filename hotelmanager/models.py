# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Bookinfo(models.Model):
    book_id = models.AutoField(primary_key=True)
    cus_id = models.IntegerField(blank=True, null=True)
    book_time = models.DateField(blank=True, null=True)
    book_idnum = models.CharField(max_length=18, blank=True, null=True)
    book_phone = models.CharField(max_length=11, blank=True, null=True)
    book_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bookinfo'


class Checkinfo(models.Model):
    check_id = models.AutoField(primary_key=True)
    book_id = models.IntegerField(blank=True, null=True)
    check_name = models.CharField(max_length=16, blank=True, null=True)
    check_idnum = models.CharField(max_length=18, blank=True, null=True)
    check_phone = models.CharField(max_length=11, blank=True, null=True)
    check_leavetime = models.DateField(blank=True, null=True)
    check_checkintime = models.DateField(db_column='check_checkInTime', blank=True, null=True)  # Field name made lowercase.
    check_statu = models.CharField(max_length=5, blank=True, null=True)
    room_id = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'checkinfo'


class Customer(models.Model):
    cus_id = models.AutoField(primary_key=True)
    cus_name = models.CharField(max_length=16, blank=True, null=True)
    cus_phone = models.CharField(max_length=11, blank=True, null=True)
    cus_password = models.CharField(max_length=20, blank=True, null=True)
    id_num = models.CharField(max_length=18, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Price(models.Model):
    room_level = models.CharField(max_length=11, blank=True, null=True)
    room_price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'price'


class Room(models.Model):
    room_id = models.CharField(primary_key=True, max_length=4)
    room_level = models.CharField(max_length=11, blank=True, null=True)
    room_pic = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room'


class Staff(models.Model):
    sta_id = models.AutoField(primary_key=True)
    sta_authority = models.CharField(max_length=6, blank=True, null=True)
    sta_passward = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff'
