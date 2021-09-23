from django.contrib import admin
from .models import Hospital, MainDoctor, Doctor, Nurses, Patient
# Register your models here.

class HospitalAdmin(admin.ModelAdmin):
    list_display = ("name", "region", "ocpo", "gov", "doctors", "maxn")
    # search_fields = ("name", "doctors", "region")
    # list_editable = ("name", "doctors")
    # list_filter = ("name", "region")

admin.site.register(Hospital, HospitalAdmin)

class MainDoctorAdmin(admin.ModelAdmin):
    list_display = ("name","pin", "birthdate", "phone")
    # search_fields = ("name", "phone", "pin")
    # list_editable = ("name", "phone")
    # list_filter = ("name", "pin")
admin.site.register(MainDoctor, MainDoctorAdmin)

class NursesAdmin (admin.ModelAdmin):
    list_display = ("name", "pin", "birthdate", "phone")
    # search_fields = ("name", "phone", "pin")
    # list_editable = ("name", "phone")
    # list_filter = ("name")
admin.site.register(Nurses,NursesAdmin)

class DoctorAdmin(admin.ModelAdmin):
    list_display = ("position", "name","pin", "birthdate", "phone","hospital","nurse")
admin.site.register(Doctor,DoctorAdmin)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("name","pin", "birthdate", "phone","hospital","doctor","nurse")
admin.site.register(Patient,PatientAdmin)
