from django.urls import path, re_path
from django.conf import settings
from . import views

app_name ='neighbourhood'

urlpatterns=[
  path('api/neighbours/',views.NeighbourhoodList.as_view(),name='neighbour'),
  path('api/users/',views.UserList.as_view(),name='users'),
  path('api/business/',views.BusinessList.as_view(),name='business'),
  path('api/profile/',views.ProfileList.as_view(),name='profiles'),
  path('api/post/',views.PostList.as_view(),name='post'),

  path('api/business/list/',views.BusinessSearch.as_view(),name='search'),

  path('api/profile/update/<int:pk>/',views.ProfileList.as_view(),name='update_profile'),
  path('api/users/update/<int:pk>/',views.UserList.as_view(),name='update_users'),
  re_path('api/business/update/(?P<pk>[0-9]+)/',views.BusinessList.as_view(),name='update_business'),
  path('api/hood/update/<int:pk>/',views.NeighbourhoodList.as_view(),name='update_neighbours'),
  path('api/post/update/<int:pk>/',views.PostList.as_view(),name='update_post'),

  path('api/delete/users/<int:pk>/',views.UserList.as_view(),name='delete_users'),
  re_path('api/delete/hood/(?P<pk>[0-9]+)/',views.NeighbourhoodList.as_view(),name='delete_neighbours'),
  path('api/delete/business/<int:pk>/',views.BusinessList.as_view(),name='delete_business'),
  path('api/delete/post/<int:pk>/',views.PostList.as_view(),name='delete_post'),
]