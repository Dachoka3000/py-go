from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hood(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    adder = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class Business(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    email = models.EmailField(max_length=254,blank=True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.name  

class Profile(models.Model):
    bio = models.TextField()
    hood = models.ForeignKey(Hood, on_delete = models.SET_NULL)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return user.username

class Post(models.Model):
    poster=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    content=models.TextField()
    date_added=models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    area=models.ForeignKey(Hood, on_delete = models.CASCADE)
    policenumber= models.CharField(max_length=200)
    policemail=models.EmailField(max_length=254)
    hospitalnumber=models.CharField(max_length=300)
    hospitalmail=models.EmailField(max_length=254)

    def __str__(self):
        return self.area.name