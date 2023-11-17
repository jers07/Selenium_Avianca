import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class AutomaticNavigation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://www.google.com/')
        
    def test_browser_navigation(self):
        driver = self.driver
        
        search_bar = driver.find_element(By.NAME, 'q')
        search_bar.clear()
        search_bar.send_keys('platzi')
        search_bar.submit()
        
        driver.back()
        sleep(2)
        driver.forward()
        sleep(2)
        driver.refresh()
    
    def tearDown(self):
        self.driver.close()
    
if __name__ == "__main__":
    unittest.main(verbosity = 2)