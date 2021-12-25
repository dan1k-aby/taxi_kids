from django.contrib import admin
from .models import Voditeli, People, Dispetchery, Order

class VoditeliAdmin(admin.ModelAdmin):
    list_display = ("id", "Name_vod", "Date_of_birth",
                    "number", "Created", "Auto", "Auto_number") 
    search_fields = ("Name",)
    list_filter = ("Created",)

class PeopleAdmin(admin.ModelAdmin):
    list_display = ("id", "Name_man", "Number")
    search_fields = ("Name",)

class DispetcheryAdmin(admin.ModelAdmin):
    list_display = ("id", "Name", "Sure_name", "Date_of_birth",
                    "Number", "Created", "Email")
    search_fields = ("Name",)
    list_filter = ("Created",)

class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "Created", "Marshrut",
                    "Status", "Order_number")
    search_fields = ("id",)




admin.site.register(Voditeli, VoditeliAdmin)
admin.site.register(People, PeopleAdmin)
admin.site.register(Dispetchery, DispetcheryAdmin)
admin.site.register(Order, OrderAdmin)
