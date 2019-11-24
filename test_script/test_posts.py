import pytest
from django.test import Client, TestCase
from django.urls import resolve, reverse
from blog.models import Post, Category, Comment
from projects.models import *
from django.contrib.auth.models import User
from django.db import *
import datetime


pytestmark = pytest.mark.django_db

@pytest.mark.django_db
class TestUsers:
    pytestmark = pytest.mark.django_db
    def test_my_user(self):
        #create user 'admin' w/o superuser
        client = Client()
        user = User(username='admin', password='qwe', is_superuser=False)
        user.save()
        me = User.objects.get(username='admin')
        assert me.is_superuser

        #response = client.get(reverse('blog_index'))
        #response.status_code
        
        #response = client.get(reverse('blog_category'))
        #response.status_code

        
        #create blog post categories
    def test_create_category(self):
        category = Category(name='Django')
        category.save()
        category2 = Category(name='Godjan')
        category2.save()
        category_count = Category.objects.count()
        assert category_count == 2
        


        #create posts, w title, body. add categories to post
        post = Post(title='POST1', body='testbodytext')
        post.save()
        post2 = Post(title='POST2', body='textbodytest')
        post2.save()
        post.categories.add(category)
        post.categories.add(category2)
        post2.categories.add(category)
        post2.categories.add(category2)
        post_count = Post.objects.count()
        assert post_count == 3

        #response = client.get(post.get_absolute_url())
        #response.status_code

        #response = client.get(reverse('blog_index'), {'q': 'testbodytext'})
        #response.context[-1]['']

        #reverse('project_index', kwargs={'project_id':6})
