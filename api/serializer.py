from rest_framework import serializers
from projects.models import Profiles
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"
        
class ProfileSerializer(serializers.ModelSerializer):
    user=UserSerializer(many=False)
    class Meta:
        model=Profiles
        #fields="__all__"
        exclude=["avatar"]