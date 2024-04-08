from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profiles(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    short_intro=models.CharField(max_length=200,blank=True,null=True)
    bio=models.TextField(max_length=300,blank=True,null=True)
    avatar=models.FileField(upload_to="images")
