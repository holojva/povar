from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class UserProfile(models.Model):
    profile = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
