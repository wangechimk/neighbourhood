from django.db import models

# Create your models here.
class Neighbourhood(models.Model):
  name = models.CharField(max_length=30)
  location = models.CharField(max_length=30)

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


class User(models.Model):
  name=models.CharField(max_length=30)
  email=models.EmailField()
  neighbourhood=models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
  

  def __str__(self):
    return self.name

  def save_user(self):
    self.save()

  def delete_user(self):
    self.delete()

class Business(models.Model):
  name=models.CharField(max_length=30)
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  email=models.EmailField()
  neighbourhood=models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def save_business(self):
    self.save()

  def delete_business(self):
    self.delete()

  @classmethod
  def find_business(cls, name):
    return cls.objects.filter(name__icontains=name)

  @classmethod
  def update_business(cls, id, name):
    update = cls.objects.filter(id=id).update(name=name)
    return update