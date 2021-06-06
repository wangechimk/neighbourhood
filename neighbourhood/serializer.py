from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import Neighbourhood,User,Business,Post,Profile
from django import forms


class BusinessSerializers(serializers.ModelSerializer):
  class Meta:
    model = Business
    fields='__all__'   

class ProfileSerializer(serializers.ModelSerializer):
  business = BusinessSerializers(many=True, read_only=True)
  # User= serializers.CharField(read_only=True)

  class Meta:
    model = Profile
    fields="__all__"

class NeighbourhoodSerializer(serializers.ModelSerializer):
  profile = ProfileSerializer(many=True, read_only=True)
  business = BusinessSerializers(many=True, read_only=True)
  class Meta:
    model = Neighbourhood
    fields='__all__'

class UserSerializer(serializers.ModelSerializer):
  email = forms.EmailField(max_length=300, help_text='Required. Inform a valid email address.')
  class Meta:
    model = User
    fields = ['username','email','password']
 
class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = "__all__" 