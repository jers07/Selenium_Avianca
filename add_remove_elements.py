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
        driver.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()
        
    def test_add_remove(self):
        driver = self.driver
        
        elements_added = int(input('how many elements will you add? :'))
        elements_removed = int(input('how many elements will you remove? :'))
        total_elements = elements_added - elements_removed
        
        add_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/button')
        
        sleep(2)
        
        for i in range(total_elements):
            add_button.click()
            
        for i in range(elements_removed):   
            try:
                delete_button = driver.find_element(By.XPATH,'//*[@id="elements"]/button')
                delete_button.click
            except:
                print('you r monkee, you are trying to delete more elements than existing')
                break
        if total_elements > 0:
            print(f'there are {total_elements} elements on screen')
        else:
            print('there are 0 elements')
        
        sleep(3)
        
        
    def tearDown(self):
        self.driver.close()
    
if __name__ == "__main__":
    unittest.main(verbosity = 2)