from django.contrib.auth.models import User
from django.db import models



class Userprof(models.Model):
    user = models.OneToOneField(User, related_name='userprof', on_delete=models.CASCADE)
   