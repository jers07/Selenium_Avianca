import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class dynamic_controls(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT,'Dynamic Controls').click()
        sleep(1)
        
    def test_dynamic(self):
        driver = self.driver
        check_box = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/form[1]/div/input')
        check_box.click()
        
        remove_add_button = driver.find_element(By.CSS_SELECTOR, '#checkbox-example > button')
        remove_add_button.click()
        
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox-example > button')))
        
        enable_disable_button = driver.find_element(By.CSS_SELECTOR,'#input-example > button')
        enable_disable_button.click()
        
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#input-example > button')))
        
        
        text_box = driver.find_element(By.CSS_SELECTOR, '#input-example > input[type=text]')
        text_box.send_keys('tu mama')
        
        enable_disable_button.click()
    
    def tearDown(self):
        self.driver.close()
    
if __name__ == "__main__":
    unittest.main(verbosity = 2)
    
    
    
    