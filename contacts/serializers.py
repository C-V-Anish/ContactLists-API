from rest_framework import serializers
from .models import Contacts

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contacts
        fields=['country_code','id','first_name','last_name','phone_number','contact_photo','is_favorite']