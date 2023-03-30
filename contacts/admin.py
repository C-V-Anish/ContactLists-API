from django.contrib import admin
from .models import Contacts

# Register your models here.
@admin.register(Contacts)
class ContactAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','country_code','phone_number','contact_photo','is_favorite']