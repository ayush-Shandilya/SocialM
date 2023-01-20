from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
User = get_user_model()
# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    id_user = models.IntegerField()
    profile_pic = models.ImageField(upload_to='profile_pic/', default = "defaultpic.png")
    location = models.CharField(max_length = 100, blank = True)
    bio = models.TextField(max_length=160, blank=True, null=True)
    def serialize(self):
        return {
            'id': self.id,
            "username": self.username,
            "profile_pic": self.profile_pic.url,
            "first_name": self.first_name,
            "last_name": self.last_name
        }
    def __str__(self):
        return self.username
    

