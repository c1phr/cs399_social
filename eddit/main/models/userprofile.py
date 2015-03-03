from django.db import models
from django.core.validators import RegexValidator

class UserProfile(models.Model):
    phoneregex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phoneregex], blank=True, max_length=15)
    first_name = models.CharField(default="", max_length=128)
    last_name = models.CharField(default="", max_length=128)
    user_name = models.CharField(default="", max_length=128)