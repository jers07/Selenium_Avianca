import unittest, csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from Madison_main_page import MainPageMadison
from Madison_Log_in import MadisonLogInPage
from Madison_create_account import MadisonCreateAccount
from ddt import ddt, data, unpack

def get_data(file_name):
    rows = []
    data_file = open(file_name, 'r')
    reader = csv.reader(data_file)
    next(reader, None)
    
    for row in reader:
        rows.append(row)
    return rows
    
    
@ddt
class MadisonTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        
    @data(*get_data('pom_Madison/database_madison.csv'))
    @unpack
    def test_a_search_mainpage(self, product, amount):
        madison = MainPageMadison(self.driver)
        madison.open()
        madison.search(product)
        print(f'the product {product} has {amount} amount')
        
        self.assertEqual(product, madison.keyword)
    
    def test_b_change_language(self):
        madison = MainPageMadison(self.driver)
        madison.open()
        madison.change_language()
    
    def test_c_login(self):
        madison_login = MadisonLogInPage(self.driver)
        madison_login.open()
        madison_login.log_user('user1234', '12345678')    
        
    def test_d_create_new_account(self):
        madison_create = MadisonCreateAccount(self.driver)
        madison_create.open()
        madison_create.create_new_user('user1234', 'user567', 'user89', 'user1234@gmail.com', '12345678', '12345678')
      
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity = 2)