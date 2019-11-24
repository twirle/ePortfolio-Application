import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest

driver = webdriver.Chrome()

def test_login_empty_fields():
    driver.get('http://localhost:8000/admin/login/?next=/admin/')
    assert "Log in | Django site admin" in driver.title
    
    elemUsername = driver.find_element_by_name("username")
    #elemUsername.clear()
    elemUsername.send_keys("admin")

    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("")
    elemPassword.send_keys(Keys.RETURN)
    message = driver.find_element_by_name("password").get_attribute("validationMessage")  
    assert message == 'Please fill out this field.'

    elemUsername.clear()
    elemPassword.send_keys("asd")
    elemPassword.send_keys(Keys.RETURN)
    message = driver.find_element_by_name("username").get_attribute("validationMessage")
    assert message == 'Please fill out this field.'

    elemPassword.clear()
    elemPassword.send_keys(Keys.RETURN)
    message = driver.find_element_by_name("username").get_attribute("validationMessage")
    assert message == 'Please fill out this field.'

def test_login_admin_wrong_password():
    driver.get('http://localhost:8000/admin/login/?next=/admin/')
    assert "Log in | Django site admin" in driver.title

    elemUsername = driver.find_element_by_name("username")
    elemUsername.send_keys("admin")
    
    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("asd")
    
    elemPassword.send_keys(Keys.RETURN)
    assert driver.find_element_by_class_name("errornote")

def test_login_admin_success():
    driver.get('http://localhost:8000/admin/login/?next=/admin/')
    assert "Log in | Django site admin" in driver.title

    elemUsername = driver.find_element_by_name("username")
    elemUsername.send_keys("admin")
    
    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("12qweasd")
    
    elemPassword.send_keys(Keys.RETURN)
    assert "Site administration" in driver.title

def new_project():
    driver.find_element_by_link_text("Add Project").click()
    elemTitle = driver.find_element_by_name("title")
    elemDescription = driver.find_element_by_name("description")
    elemTechnology = driver.find_element_by_name("technology")

    message = driver.find_element_by_name("description").get_attribute("validationMessage")
    elemTitle.send_keys(Keys.RETURN)
    #elemSave = driver.find_element_by_name("_save").click()
    assert message == 'This field is required.'

    elemTitle.send_keys("title")
    elemTitle.send_keys(Keys.RETURN)
    assert message == 'This field is required.'

    elemDescription.send_keys("desc")
    elemTitle.send_keys(Keys.RETURN)
    assert message == 'This field is required.'

    elemTechnology.send_keys("technology")
    elemTechnology.send_keys(Keys.RETURN)
    assert message == 'This field is required.'

def edit_project():
    driver.get('http://localhost:8000/admin/projects/project/9/change/')
    elemDescription = driver.find_element_by_name("description")
    elemDescription.clear()
    elemTitle.send_keys(Keys.RETURN)
    assert driver.find_element_by_class_name("messagelist")


def new_user():
    driver.get('http://localhost:8000/admin/auth/user/add/')
    elemUsername = driver.find_element_by_name("username")
    elemPassword1 = driver.find_element_by_name("password1")
    elemPassword2 = driver.find_element_by_name("password2")

    
    elemUsername.send_keys(Keys.RETURN)
    assert message == 'This field is required.'
    
    elemUsername.send_keys("user")
    elemUsername.send_keys(Keys.RETURN)
    message = driver.find_element_by_name("password1").get_attribute("validationMessage")
    assert message == 'This field is required.'

    elemPassword1.send_keys("123")
    elemUsername.send_keys(Keys.RETURN)
    message = driver.find_element_by_name("password2").get_attribute("validationMessage")
    assert message == 'This field is required.'

    elemPassword1.clear()
    elemPassword2.send_keys("123")
    elemUsername.send_keys(Keys.RETURN)
    message = driver.find_element_by_name("password1").get_attribute("validationMessage")
    assert message == 'This field is required.'

    elemPassword1.send_keys("123")
    elemUsername.send_keys(Keys.RETURN)
    message = driver.find_element_by_name("password2").get_attribute("validationMessage")
   assert message == 'This field is required. This password is too short. It must contain at least 8 characters. This password is too common. This password is entirely numeric.'

    elemUsername.clear()
    elemPassword1.clear()
    elemPassword2.clear()

    elemUsername.send_keys("admin")
    elemPassword1.send_keys("12qweasd")
    elemPassword2.send_keys("12qweasd")
    elemUsername.send_keys(Keys.RETURN)
    message = driver.find_element_by_name("username").get_attribute("validationMessage")
    assert message == 'A user with that username already exists.'

