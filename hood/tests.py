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

    

class ContactTestCase(TestCase):
    '''
    TestCase that runs test for contact model objects
    '''
    

