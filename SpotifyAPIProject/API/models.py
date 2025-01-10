from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from cryptography.fernet import Fernet
from django.conf import settings

# Create your models here.