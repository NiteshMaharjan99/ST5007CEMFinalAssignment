from django.test import TestCase
from django.test import Client, TestCase, SimpleTestCase
from django.urls import reverse,resolve
from ecom.views import *
from django.contrib.auth.models import User
from .models import *

# Create your tests here.
# class TestUrls(SimpleTestCase):
#     def text_index_url(self):
#         url=reverse('store')
#         self.assertEquals(resolve(url).func,store)

    # def test_cart_url(self):
    #     cartItems = Order.()
    #     url=reverse('cart')

    #     self.assertEquals(resolve(url).func,edit)

# class TestViews(TestCase):
#     def test_index(self):
#         user=User.objects.create(username='nitesh')
#         user.set_password('maharjan100')
#         user.save()
#         client = Client()
#         logged_in=client.login(username='nitesh',password="maharjan100")


#         # login_required not needed
#         response=client.get(reverse('store'))
#         print(response) # status_code == 200
#         self.assertEquals(response.status_code,200)
#         self.assertTemplateUsed(response,"store")

# class TestUrls(SimpleTestCase):
#     def text_store_url(self):
#         url=reverse('')
#         self.assertEquals(resolve(url).func,store)