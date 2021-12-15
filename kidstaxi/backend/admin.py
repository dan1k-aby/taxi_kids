from django.contrib import admin
from .models import Voditeli, People, Dispetchery

class VoditeliAdmin(admin.ModelAdmin):
    list_display = ("id", "Name", "Sure_name", "Date_of_birth",
                    "number", "Created", "Auto", "Auto_number") 
    search_fields = ("Name",)
    list_filter = ("Created",)

class PeopleAdmin(admin.ModelAdmin):
    list_display = ("id", "Name", "Sure_name", "Number")
    search_fields = ("Name",)

class DispetcheryAdmin(admin.ModelAdmin):
    list_display = ("id", "Name", "Sure_name", "Date_of_birth",
                    "Number", "Created", "Email")
    search_fields = ("Name",)
    list_filterc = ("Created",)


admin.site.register(Voditeli, VoditeliAdmin)
admin.site.register(People, PeopleAdmin)
admin.site.register(Dispetchery, DispetcheryAdmin)
