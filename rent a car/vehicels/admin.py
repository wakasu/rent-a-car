from django.contrib import admin
from vehicels.models import vehicel


# Register your models here.


class VehicelAdmin(admin.ModelAdmin):
    pass


admin.site.register(vehicel, VehicelAdmin)