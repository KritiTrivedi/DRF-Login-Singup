from django.db import models
import uuid
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.

class User(models.Model):
    id= models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    email = models.EmailField(max_length=35,null=True, blank=True)
    password = models.CharField(max_length=200)

    class Meta:
        db_table = 'User'
       




