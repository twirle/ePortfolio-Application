import pytest
from django.test import Client, TestCase
from django.db import *
from django.contrib.auth.models import User

class BaseTestCase(TestCase):
    
    def setUp(self):
       #Class setup.
        self.client = Client()
        self.index_url = '/'
        self.login()

    def create_user(self):
        #Create user and returns username, password tuple.
        username, password = '', ''
        user = User.objects.get_or_create(
            username=username,
            email='admin@test.com',
            is_superuser=True
        )[0]
        user.set_password(password)
        user.save()
        self.user = user
        return (username, password)

    def login(self):
        #Log in client session.
        username, password = self.create_user()
        self.client.login(username=username, password=password)


class AdminTestCase(BaseTestCase):

    def test_responsible_list(self):
        response = self.client.get('/admin/responsilbe_list/')
        # assertions....
