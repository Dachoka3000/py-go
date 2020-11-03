from django.test import TestCase
from .models import Hood,Post,Profile,Contact,Business
from django.contrib.auth import get_user_model

# Create your tests here.
class HoodTestCase(TestCase):
    '''
    TestCase that runs tests for hood model objects
    '''
    def test_create_model(self,name,location,occupants,adder):
        User=get_user_model()
        self.daisy = User(username = "daisy", email="daisy@email.com", password = "mypassword")
        self.daisy.save()
        name="duckistan"
        location="islamabad"
        occupants=678
        adder=self.daisy

        self.hoodie=Hood.create_neighbourhood(name=name,location=location,occupants=occupants,adder=adder)
        self.assertTrue(isinstance(self.hoodie,Hood))

    

class ContactTestCase(TestCase):
    '''
    TestCase that runs test for contact model objects
    '''
    def setUp(self):
        User = get_user_model()
        self.daisy = User(username = "daisy", email="daisy@email.com", password = "password")
        self.daisy.save()
        self.hood = Hood(name="local",location="area",occupants=5,adder=self.daisy)
        self.hood.save()
        self.contact=Contact(area=self.hood,policenumber="23456",policemail="police@email.com",hospitalnumber="465768",hospitalmail="hospital@email.com")
    
    def test_instance(self):
        self.assertTrue(isinstance(self.contact,Contact))

    def test_save_method(self):
        self.contact.save_contact()
        contacts=Contact.objects.all()
        self.asertTrue(len(contacts)>0)

    def test_delete_method(self):
        self.contact.save_contact()
        self.contact=Contact.objects.get(policenumber="23456")
        self.contact.delete_contact()
        contacts=Contact.objects.all()
        self.assertTrue(len(contacts)==0)

class PostTestCase(TestCase):
    '''
    Test case that runs test cases for post model objects
    '''
    def setUp(self):
        User = get_user_model()
        self.daisy = User(username = "daisy", email="daisy@email.com", password = "password")
        self.daisy.save()
        self.hood = Hood(name="local",location="area",occupants=5,adder=self.daisy)
        self.hood.save()
        self.post=Post(poster=self.daisy,area=self.hood,title="testing title",content="this is a test")

    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))

    def test_save_method(self):
        self.post.save_post()
        posts=Post.objects.all()
        self.assertTrue(len(posts)>0)

    def test_delete_method(self):
        self.post.save_post()
        self.post=Post.objects.get(title="testing title")
        self.post.delete_post()
        posts=Post.objects.all()
        self.assertTrue(len(posts)==0)



class ProfileTestCase(TestCase):
    '''
    Test case class that runs test cases for profile model objects
    '''

    def setUp(self):
        User = get_user_model()
        self.daisy = User(username = "daisy", email="daisy@email.com", password = "password")
        self.daisy.save()
        self.hood = Hood(name="local",location="area",occupants=5,adder=self.daisy)
        self.hood.save()
        self.profile = Profile(bio="love life",hood=self.hood,user=self.daisy)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_update_method(self):
        self.profile.save_profile()
        self.profile = Profile.objects.filter(bio = 'love life').update(bio = 'easy')
        self.profile_update = Profile.objects.get(user=self.daisy)
        self.assertTrue(self.profile_update.bio== 'easy')

    def test_delete_method(self):
        self.profile.save_profile()
        self.profile=Profile.objects.get(bio='easy')
        self.profile.delete_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)==0)