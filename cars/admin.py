from django.contrib import admin
from .models import Car
# Register your models here.



class CarAdmin(admin.ModelAdmin):
    # fields = ['year','brand'] ## changes the field order in the admin interface
    fieldsets = [
        ('TIME INFORMATION', {'fields': ['year']} ),
        ('CAR INFORMATION', {'fields': ['brand']})
    ] ## Puts fields into categories or sections

admin.site.register(Car, CarAdmin)