from django.urls import path, re_path
from django.conf import settings
from . import views
from rest_framework.authtoken.views import ObtainAuthToken

app_name ='neighbourhood'

urlpatterns=[
  path('api/neighbours/',views.NeighbourhoodList.as_view(),name='neighbour'),
  path('api/users/',views.UserList.as_view(),name='users'),
  path('api/business/',views.BusinessList.as_view(),name='business'),
  path('api/profile/',views.ProfileList.as_view(),name='profiles'),
  path('api/post/',views.PostList.as_view(),name='post'),
  path('authlogin/', ObtainAuthToken.as_view(), name="authlogin"),

  path('api/business/list/',views.BusinessSearchList.as_view(),name='search'),

  path('api/update/profile/<int:pk>/',views.ProfileList.as_view(),name='update_profile'),
  path('api/update/users<int:pk>/',views.UserList.as_view(),name='update_users'),
  re_path('api/update/business(?P<pk>[0-9]+)/',views.BusinessList.as_view(),name='update_business'),
  path('api/update/hood/<int:pk>/',views.NeighbourhoodList.as_view(),name='update_neighbours'),
  path('api/update/post/<int:pk>/',views.PostList.as_view(),name='update_post'),

  path('api/delete/users/<int:pk>/',views.UserList.as_view(),name='delete_users'),
  re_path('api/delete/hood/(?P<pk>[0-9]+)/',views.NeighbourhoodList.as_view(),name='delete_neighbours'),
  path('api/delete/business/<int:pk>/',views.BusinessList.as_view(),name='delete_business'),
  path('api/delete/post/<int:pk>/',views.PostList.as_view(),name='delete_post'),

  path('api/single-hood/<int:pk>/',views.singleHood.as_view()),
  # path('api/single-business/<int:pk>/',views.singleBusiness.as_view()),
  path('api/single-post/<int:pk>/',views.singlePost.as_view()),
]