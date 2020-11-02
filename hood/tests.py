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

        self.hoodie=Hood.create_neighbourhood(self,name,location,occupants,adder)
        self.assertTrue(isinstance(self.hoodie,Hood))

    

# class ContactTestCase(TestCase):
#     '''
#     TestCase that runs test for contact model objects
#     '''


class ProfileTestCase(TestCase):
    '''
    Test case class that runs test cases for profile model objects
    '''

    def setUp(self):
        User = get_user_model()
        self.daisy = User(username = "daisy", email="daisy@email.com", password = "password")
        self.daisy.save()
        self.profile = Profile(bio="love life","daisy@email.com",user=self.daisy)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_update_method(self):
        self.profile.save_profile()
        self.profile = Profile.objects.filter(contact = 'daisy@email.com').update(contact = 'maisy@email.com')
        self.profile_update = Profile.objects.get(bio="love life")
        self.assertTrue(self.profile_update.contact== 'maisy@email.com')

    def test_delete_method(self):
        self.profile.save_profile()
        self.profile=Profile.objects.get(bio='love life')
        self.profile.delete_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)==0)