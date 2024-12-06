from django.contrib import admin

# Register your models here.
from .models import Register,VehicleInfo

admin.site.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'email')  # Columns to display in admin list view
    search_fields = ('name', 'phone', 'email')           # Searchable fields
@admin.register(VehicleInfo)
class VehicleInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'wheel_type', 'vehicle_no')  # Show associated user
    list_filter = ('wheel_type',)                       # Add filter for wheel type
    search_fields = ('user__name', 'vehicle_no')        # Enable search by user name or vehicle number