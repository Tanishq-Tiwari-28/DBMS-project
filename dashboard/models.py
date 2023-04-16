from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.models import User
# from dashboard.managers import CustomUserManager


class Admins(models.Model):
    # Field name made lowercase.
    admin_id = models.AutoField(db_column='Admin_id', primary_key=True)
    email = models.CharField(unique=True, max_length=50)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    contact = models.CharField(max_length=12)
    # Field name made lowercase.
    verified_driver = models.IntegerField(
        db_column='verified_Driver', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Admins'


class Customer(models.Model):
    # Field name made lowercase.
    customer_id = models.AutoField(db_column='Customer_id', primary_key=True)
    pass_word = models.CharField(db_column='Pass_word', max_length=128)
    email = models.CharField(unique=True, max_length=50)
    firstname = models.CharField(max_length=200)
    middlename = models.CharField(max_length=200, blank=True, null=True)
    lastname = models.CharField(max_length=200)
    contact = models.CharField(max_length=12)
    dob = models.DateField(db_column='DOB')  # Field name made lowercase.
    notifications = models.CharField(max_length=200, blank=True, null=True)
    current_location_lat = models.FloatField(blank=True, null=True)
    current_location_long = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Customer'


class CustomerDetails(models.Model):
    # Field name made lowercase.
    customer = models.ForeignKey(
        'Customer', models.DO_NOTHING, db_column='Customer_id', blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'customer_details'


class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True)
    pass_word = models.CharField(db_column='Pass_word', max_length=128)
    email = models.CharField(unique=True, max_length=50)
    firstname = models.CharField(max_length=200)
    middlename = models.CharField(max_length=200, blank=True, null=True)
    lastname = models.CharField(max_length=200)
    contact = models.CharField(max_length=12)
    dob = models.DateField(db_column='DOB')  # Field name made lowercase.
    verified = models.IntegerField(blank=True, null=True, default=0)
    verified_by = models.ForeignKey(
        'Admins', models.DO_NOTHING, db_column='verified_by')
    notifications = models.CharField(max_length=200, blank=True, null=True)
    current_location_lat = models.FloatField(blank=True, null=True)
    current_location_long = models.FloatField(blank=True, null=True)
    ratings = models.IntegerField(blank=True, null=True)
    available = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Driver'


class DriverDetails(models.Model):
    driver = models.ForeignKey(
        'Driver', models.DO_NOTHING, blank=True, null=True)
    contact = models.CharField(
        max_length=100, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'driver_details'


class Verifies(models.Model):
    driver = models.OneToOneField(
        'Driver', models.DO_NOTHING, blank=True, primary_key=True)
    # Field name made lowercase.
    admin = models.ForeignKey(
        'Admins', models.DO_NOTHING, db_column='Admin_id', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'verifies'
        unique_together = (('driver', 'admin'),)


class Vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    owner_firstname = models.CharField(max_length=100)
    owner_middlename = models.CharField(max_length=100, blank=True, null=True)
    owner_lastname = models.CharField(max_length=100)
    engine_no = models.CharField(max_length=100)
    date_of_manufacture = models.DateField()
    validity = models.DateField()
    car_model = models.CharField(max_length=100)
    car_make = models.CharField(max_length=100)
    car_type = models.CharField(max_length=100)
    driver = models.ForeignKey(
        'Driver', models.DO_NOTHING, blank=True, null=True)
    # Field name made lowercase.
    customer = models.ForeignKey(
        'Customer', models.DO_NOTHING, db_column='Customer_id', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicle'


class Trip(models.Model):
    trip_id = models.AutoField(primary_key=True)
    pickup_location = models.CharField(max_length=100)
    drop_location = models.CharField(max_length=100)
    payable_amount = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True)
    pickup_time = models.TimeField(blank=True, null=True)
    drop_time = models.TimeField(blank=True, null=True)
    mode_of_transaction = models.CharField(
        max_length=100, blank=True, null=True)
    ride_status = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trip'


class Requests(models.Model):
    trip = models.OneToOneField(
        'Trip', models.DO_NOTHING, blank=True, primary_key=True)
    # Field name made lowercase.
    customer = models.ForeignKey(
        'Customer', models.DO_NOTHING, db_column='Customer_id', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requests'
        unique_together = (('trip', 'customer'),)


class AcceptOrDecline(models.Model):
    driver = models.ForeignKey(
        'Driver', models.DO_NOTHING, blank=True, null=True)
    trip = models.OneToOneField(
        'Trip', models.DO_NOTHING, blank=True, primary_key=True)
    is_accepted = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'accept_or_decline'
        unique_together = (('trip', 'driver'),)


class Rating(models.Model):
    trip = models.OneToOneField('Trip', models.DO_NOTHING, primary_key=True)
    stars = models.IntegerField(blank=True, null=True)
    complaints = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rating'


class Sedan(models.Model):
    comfort_level = models.IntegerField(blank=True,)
    vehicle = models.OneToOneField(
        'Vehicle', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'SEDAN'


class Suv(models.Model):
    roadtype = models.CharField(max_length=100, blank=True, null=True)
    vehicle = models.OneToOneField(
        'Vehicle', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'SUV'


class Hatchback(models.Model):
    tot_passengers = models.IntegerField(blank=True, null=True)
    vehicle = models.OneToOneField(
        'Vehicle', models.DO_NOTHING,   primary_key=True)

    class Meta:
        managed = False
        db_table = 'HATCHBACK'
