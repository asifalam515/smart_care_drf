from django.contrib import admin
from .models import AvailableTime,Doctor,Designation,Specialization,Review
# Register your models here.
admin.site.register(AvailableTime)
class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',),}
    
class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',),}    


admin.site.register(Doctor)
admin.site.register(Designation,DesignationAdmin)
admin.site.register(Specialization,SpecializationAdmin)
admin.site.register(Review)