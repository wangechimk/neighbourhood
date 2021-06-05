from django.urls import path, re_path
from django.conf import settings
from . import views

app_name ='neighbourhood'

urlpatterns=[
  path('api/neighbours/',views.NeighbourhoodList.as_view(),name='neighbour'),
  path('api/users/',views.UserList.as_view(),name='users'),
  path('api/business/',views.BusinessList.as_view(),name='business'),
]