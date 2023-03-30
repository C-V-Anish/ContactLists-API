from rest_framework import serializers
from .models import Contacts

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contacts
        fields=['first_name','last_name','country_code','phone_number','contact_photo','is_favorite']