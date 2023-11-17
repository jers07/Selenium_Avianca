import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep

class MainPageMadison(object):
    def __init__(self, driver):
        self._driver = driver
        self._url = 'http://demo-store.seleniumacademy.com/'
        self.search_locator = 'q'
        
    @property
    def is_open(self):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))
        return True
    
    @property
    def keyword(self):
        input_field = self._driver.find_element(By.NAME, 'q')
        return input_field.get_attribute('value')
    
    def open(self):
        self._driver.get(self._url)
        
    def type_search(self, keyword):
        input_field = self._driver.find_element(By.NAME, 'q')
        input_field.send_keys(keyword)
    
    def click_submit(self):
        input_field = self._driver.find_element(By.NAME, 'q')
        input_field.submit()
    
    def search(self, keyword):
        self.type_search(keyword)
        self.click_submit()
        
    def change_language(self):
        dropdown_language = Select(self._driver.find_element(By.ID, 'select-language'))
        dropdown_language.select_by_visible_text('German')
        sleep(1)
        dropdown_language = Select(self._driver.find_element(By.ID, 'select-language'))
        dropdown_language.select_by_visible_text('English')
        sleep(1)
        dropdown_language = Select(self._driver.find_element(By.ID, 'select-language'))
        dropdown_language.select_by_visible_text('French')

        
        