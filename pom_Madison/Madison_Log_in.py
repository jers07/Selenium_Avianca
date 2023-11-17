import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep

class MadisonLogInPage(object):
    def __init__(self, driver):
        self._driver = driver
        self._url = 'http://demo-store.seleniumacademy.com/customer/account/login/'
        self.search_locator = 'email'
        
    @property
    def is_open(self):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'email')))
        return True
    
    @property
    def user(self):
        input_field_user = self._driver.find_element(By.ID, 'email')
        return input_field_user.get_attribute('value')
    
    @property 
    def password(self):
        input_field_password = self._driver.find_element(By.ID, 'pass')
        return input_field_password.get_attribute('value')
    
    def open(self):
        self._driver.get(self._url)
                     
    def fill_fields(self, user, password):
        email_field = self._driver.find_element(By.ID, 'email')
        email_field.send_keys(user)
        sleep(1)
        password_field = self._driver.find_element(By.ID, 'pass')
        password_field.send_keys(password)
        sleep(1)
    
    def click_submit(self):
        submit_button = self._driver.find_element(By.CSS_SELECTOR, '#send2 > span > span')
        submit_button.click()
    
    def log_user(self, user, password):
        self.fill_fields(user, password)
        self.click_submit()
        
    
    
        
        