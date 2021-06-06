from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from os import name

# Create your models here.
class Neighbourhood(models.Model):
  name = models.CharField(max_length=50)
  location = models.CharField(max_length=50)
  occupants_count=models.IntegerField(default=0)
  description=models.TextField(max_length=200 ,null=True)
  # admin=models.ForeignKey(User ,related_name= 'admin' ,on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def save_neighbourhood(self):
    self.save()

  def delete_neighbourhood(self):
    self.delete()

  @classmethod
  def find_neighbourhood(cls, name):
    return cls.objects.filter(name__icontains=name)

  @classmethod
  def update_neighbourhood(cls, id, name):
    update = cls.objects.filter(id=id).update(name=name)
    return update

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=80, blank=True)
    bio = models.TextField(max_length=254, blank=True)
    profile_picture = models.ImageField(upload_to='images/', default='default.png')
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)

    def __str__(self):
        return f'{self.user.username} profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Business(models.Model):
  business_name=models.CharField(max_length=50,null=True)
  business_desc=models.TextField(max_length=200 ,null=True ,blank=True)
  User=models.ForeignKey(User,on_delete=models.CASCADE,related_name='business_user',null=True)
  business_email=models.EmailField(default='wangechik@gmail.com')
  neighbourhood=models.ForeignKey(Neighbourhood,related_name='business_hood',on_delete=models.CASCADE,null=True)

  def __str__(self):
    return self.business_name

  def save_business(self):
    self.save()

  def delete_business(self):
    self.delete()

  @classmethod
  def find_business(cls, name):
    return cls.objects.filter(business_name__icontains=name)

  @classmethod
  def update_business(cls, id, name):
    update = cls.objects.filter(id=id).update(name=name)
    return update


class Post(models.Model):
    title = models.CharField(max_length=120, null=True)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_owner')
    hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='hood_post')   

    def __str__(self):
      return self.post_name   