from django.db import models
from django.contrib.auth.models import AbstractUser,Group

class AppUser(AbstractUser):
    name=models.CharField(max_length=60,verbose_name='first name',blank=False)
    email=models.EmailField(max_length=254,verbose_name='email address',blank=False)
    
    def __str__(self):
        return self.username