from django.db import models
from django.contrib.auth.models import AbstractUser
from common.db import BaseModel
# Create your models here.

class User(AbstractUser):
    phone = models.CharField(verbose_name='手机号', default='', max_length=11)
    avatar = models.ImageField(verbose_name='用户头像',upload_to='avatar/', blank=True, null=True)