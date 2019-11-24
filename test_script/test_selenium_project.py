import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest

driver = webdriver.Chrome()

def new_project():
    driver.get('http://localhost:8000/admin/projects/project/')
    assert "Site administration" in driver.title
    
    driver.find_element_by_link_text("Add Project").click()

    
