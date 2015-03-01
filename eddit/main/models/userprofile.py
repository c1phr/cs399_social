from django.db import models
from django.core.validators import RegexValidator

class UserProfile(models.Model):
    #user = models.OneToOneField(User)
    phoneregex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phonenumber = models.CharField(validators=[phoneregex], blank=True, max_length=15)