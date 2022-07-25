from django.test import TestCase
from django.test import Client, TestCase, SimpleTestCase
from django.urls import reverse,resolve
from account.views import *
from django.contrib.auth.models import User

# Create your tests here.
class TestUrls(SimpleTestCase):
    # passed test
    def test_index_url(self):
        url=reverse('userLogin')
        self.assertEquals(resolve(url).func,userLogin)
    # passed test
    def test_userRegister_url(self):
        url=reverse('userRegister')
        self.assertEquals(resolve(url).func,userRegister)
    
    # failed test
    def test_userRegister_url(self):
        url=reverse('userRegister')
        self.assertEquals(resolve(url).func,userLogin)