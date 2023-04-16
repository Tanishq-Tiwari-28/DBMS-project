from django.contrib import admin
from dashboard.models import Admins, Customer, CustomerDetails, Driver, DriverDetails, Verifies, Vehicle, Trip, AcceptOrDecline, Requests, Rating, Sedan, Suv, Hatchback
# Register your models here
admin.site.register(Admins)
admin.site.register(Customer)
admin.site.register(CustomerDetails)
admin.site.register(Driver)
admin.site.register(DriverDetails)
admin.site.register(Verifies)
admin.site.register(Vehicle)
admin.site.register(Trip)
admin.site.register(AcceptOrDecline)
admin.site.register(Requests)
admin.site.register(Rating)
admin.site.register(Sedan)
admin.site.register(Suv)
admin.site.register(Hatchback)
