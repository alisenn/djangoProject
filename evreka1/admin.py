from django.contrib import admin
from .models import NavigationRecord, Vehicle

# Register your models here.
admin.site.register(NavigationRecord)
admin.site.register(Vehicle)