from django.contrib import admin
from .models import Voditeli

class VoditeliAdmin(admin.ModelAdmin):
    list_display = ("id", "Name", "Sure_name", "Date_of_birth",
                    "number", "Created", "Auto", "Auto_number") 
    search_fields = ("Name",)
    list_filter = ("Created",)

admin.site.register(Voditeli, VoditeliAdmin)
