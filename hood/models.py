from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Hood(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    occupants = models.IntegerField(null=True)
    adder = models.ForeignKey(User, on_delete = models.CASCADE, related_name ="hoods")

    def create_neighbourhood(self,name,location,occupants,adder):
        new_neighbourhood= Hood.objects.create(name=name,location=location,occupants=occupants,adder=adder)
        return new_neighbourhood

    def save_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    @classmethod
    def find_neighbourhoood(cls,neighbourhod_id):
        found_neighbourhood=cls.objects.filter(id=neighbourhod_id)
        return found_neighbourhood

    @classmethod
    def update_neighbourhood(cls,name,new_name):
        hood=cls.objects.filter(name=name).update(name=new_name)
        return hood

    @classmethod
    def update_occupants(cls,hood_id, new_occupants):
        hood=cls.objects.filter(id=hood_id).update(occupants=new_occupants)
        return hood

    def __str__(self):
        return self.name

class Business(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    email = models.EmailField(max_length=254,blank=True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name="businesses")
    area = models.ForeignKey(Hood, on_delete=models.CASCADE, related_name="businesses",null=True)

    def create_business(self,name,description,email,owner,area):
        new_business=Business.objects.create(name=name,description=description,email=email,owner=owner,area=area)
        return new_business


    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls,business_id):
        found_business=cls.objects.filter(id=business_id)
        return found_business

    @classmethod
    def update_business(cls,name,new_name):
        biz=cls.objects.filter(name=name).update(name=new_name)
        return biz
    
  

    def __str__(self):
        return self.name  


class Profile(models.Model):
    avatar= CloudinaryField("avatar",blank=True, null=True)
    bio = models.TextField()
    hood = models.ForeignKey(Hood, on_delete = models.CASCADE, related_name="userprofiles")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userprofle")

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.user.username

class Post(models.Model):
    poster=models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    area=models.ForeignKey(Hood, on_delete=models.CASCADE, related_name="posts", null=True)
    title=models.CharField(max_length=300)
    content=models.TextField()
    image= CloudinaryField("image",blank=True, null=True)
    date_added=models.DateField(auto_now_add=True,null=True)

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def __str__(self):
        return self.title

class Contact(models.Model):
    area=models.ForeignKey(Hood, on_delete = models.CASCADE, related_name="contacts")
    policenumber= models.CharField(max_length=200)
    policemail=models.EmailField(max_length=254)
    hospitalnumber=models.CharField(max_length=300)
    hospitalmail=models.EmailField(max_length=254)

    def save_contact(self):
        self.save()

    def delete_contact(self):
        self.delete()

    def __str__(self):
        return self.area.name