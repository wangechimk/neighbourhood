from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *

# Create your views here.
class NeighbourhoodList(APIView):
  def get(self,request,format=None):
    neighbourhood= Neighbourhood.objects.all()
    serializers=NeighbourhoodSerializer(neighbourhood, many=True)
    return Response(serializers.data)

class UserList(APIView):
  def get(self,request,format=None):
    users=User.objects.all()
    serializers=UserSerializer(users, many=True)
    return Response(serializers.data)  

class BusinessList(APIView):
  def get(self, request,format=None):
    business=Business.objects.all()
    serializers=BusinessSerializers(business, many=True)
    return Response(serializers.data)      