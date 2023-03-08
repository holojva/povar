from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class SubscribeModel(models.Model):
    self_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sub")
    other_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")