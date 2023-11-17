import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from time import sleep

class MadisonCreateAccount(object):
    def __init__(self, driver):
        self._driver = driver
        self._url = "http://demo-store.seleniumacademy.com/customer/account/create/"
        self.search_locator = 'firstname'
    
    @property
    def is_open(self):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'firstname')))
    
    '''
    @property
    def first_name(self):
        input_field_first_name = self._driver.find_element(By.ID, 'firstname')
        return input_field_first_name.get_attribute('value')
    @property
    def middle_name(self):
        input_field_middle_name = self._driver.find_element(By.ID,'middlename')
        return input_field_middle_name.get_attribute('value')
    @property
    def last_name(self):
        input_field_last_name = self._driver.find_element(By.ID,'lastname')
        return input_field_last_name.get_attribute('value')
    @property
    def email_address(self):
        input_field_email_address = self._driver.find_element(By.ID, 'email_address')
        return input_field_email_address.get_attribute('value')
    @property
    def password(self):
        input_field_password = self._driver.find_element(By.ID, 'password')
        return input_field_password.get_attribute('value')
    @property
    def confirm_password(self):
        input_field_confirm_password = self._driver.find_element(By.ID, 'confirmation')
        return input_field_confirm_password.get_attribute('value')
    '''
    def open(self):
        self._driver.get(self._url)
        
    def fill_fields(self, first_name, middle_name, last_name, email_address, password, confirm_password):
        first_name_field = self._driver.find_element(By.ID, 'firstname')
        first_name_field.send_keys(first_name)
        sleep(1)
        middle_name_field = self._driver.find_element(By.ID, 'middlename')
        middle_name_field.send_keys(middle_name)
        sleep(1)
        last_name_field = self._driver.find_element(By.ID, 'lastname')
        last_name_field.send_keys(last_name)
        sleep(1)
        email_address_field = self._driver.find_element(By.ID, 'email_address')
        email_address_field.send_keys(email_address)
        sleep(1)
        password_field = self._driver.find_element(By.ID, 'password')
        password_field.send_keys(password)
        sleep(1)
        confirm_password_field = self._driver.find_element(By.ID, 'confirmation')
        confirm_password_field.send_keys(confirm_password)
        sleep(1)
    
    def register_user(self):
        register_button = self._driver.find_element(By.CSS_SELECTOR, '#form-validate > div.buttons-set > button > span > span')
        register_button.click()
    
    def create_new_user(self, first_name, middle_name, last_name, email_address, password, confirm_password):
        
        self.fill_fields(first_name, middle_name, last_name, email_address, password, confirm_password)
        self.register_user()
        