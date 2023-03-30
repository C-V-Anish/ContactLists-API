from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contacts(models.Model):
    owner=models.ForeignKey(to=User,on_delete=models.CASCADE)
    country_code=models.CharField(max_length=32)
    first_name=models.CharField(max_length=32)
    last_name=models.CharField(max_length=32)
    phone_number=models.CharField(max_length=32)
    contact_photo=models.URLField(null=True)
    is_favorite=models.BooleanField(default=False)
    