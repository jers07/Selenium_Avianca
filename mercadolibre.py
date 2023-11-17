import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class MercadoLibreTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window
        driver.get('https://www.mercadolibre.com/')
        driver.find_element(By.ID, 'CO').click()
        
    def test_filter_playstation4(self):
        driver = self.driver
        
        search_bar = driver.find_element(By.ID,'cb1-edit')
        search_bar.clear()
        search_bar.send_keys('Playstation 4')
        search_bar.submit()
        sleep(2)
        
        place_filter = driver.find_element(By.XPATH, '/html/body/main/div/div[2]/aside/section/div[11]/ul/li[1]/a/span[1]')
        driver.execute_script("arguments[0].click();", place_filter)
        sleep(2)
        
        condition_filter = driver.find_element(By.XPATH,"/html/body/main/div/div[2]/aside/section[2]/div[5]/ul/li[1]/a/span[1]")
        driver.execute_script("arguments[0].click();", condition_filter)
        sleep(2)
        
        droopdown_filter = driver.find_element(By.ID, 'react-aria-:Rlh9b9:-trigger')
        droopdown_filter.click()
        higher_price = driver.find_element(By.CSS_SELECTOR,'#react-aria-\:Rlh9b9\:-menu-list-option-price_desc > div > div > span')
        higher_price.click()
        
        articles = []
        prices = []
        
        for i in range(5):
            article_name = driver.find_element(By.XPATH,f'/html/body/main/div/div[2]/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2').text
            articles.append(article_name)
            article_price = driver.find_element(By.XPATH, f'/html/body/main/div/div[2]/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[3]').text
            prices.append(article_price)
        
        print(articles, prices)
        

    def tearDown(self):
        self.driver.close()
if __name__ == '__main__':
    unittest.main(verbosity = 2)