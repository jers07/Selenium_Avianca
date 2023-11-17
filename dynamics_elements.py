import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class AddRemoveElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT,'Disappearing Elements').click()
        
        
    def test_name_elements(self):
        driver = self.driver
        
        options = []
        menu = 5
        tries = 0
        
        while len(options) < 5:
            options.clear()
            
            for i in range(menu):
                try:
                    option_name = driver.find_element(By.XPATH,f'//*[@id="content"]/div/ul/li[{i + 1}]/a')
                    options.append(option_name.text)
                    print(options)
                    tries += 1
                except:
                    print(f'option number {i + 1} is not found')
                    driver.refresh()
                    
        print(f'finished in {tries}')
    
    def tearDown(self):
        self.driver.close()
    
if __name__ == "__main__":
    unittest.main(verbosity = 2)