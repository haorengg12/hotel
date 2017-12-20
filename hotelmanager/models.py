# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bookinfo(models.Model):
    book_id = models.AutoField(primary_key=True)
    cus_id = models.IntegerField(blank=True, null=True)
    book_time = models.DateTimeField(blank=True, null=True)
    book_idnum = models.CharField(max_length=18, blank=True, null=True)
    book_phone = models.CharField(max_length=11, blank=True, null=True)
    book_num = models.IntegerField(blank=True, null=True)
    book_price = models.FloatField(blank=True, null=True)

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
    id_num = models.CharField(max_length=18, blank=True, null=True)
    cus_phone = models.CharField(max_length=11)
    cus_password = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'
        unique_together = (('cus_id', 'cus_phone'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
