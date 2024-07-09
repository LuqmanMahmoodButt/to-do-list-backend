
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.

class User(AbstractUser):
    # abstract user already requires username and password, so we juat have to add the extra fields that we want for our users 

    email = models.CharField(max_length=50, unique=True)


    