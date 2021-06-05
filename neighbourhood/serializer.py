from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Neighbourhood,User,Business


class NeighbourhoodSerializer(serializers.ModelSerializer):
  class Meta:
    model = Neighbourhood
    fields=['name','location']

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    exclude = ['neighbourhood']  

class BusinessSerializers(serializers.ModelSerializer):
  class Meta:
    model = Business
    fields=['name','email']      