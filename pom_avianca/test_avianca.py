import unittest, csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from ddt import ddt,data,unpack
from avianca_main_page import AviancaMainPage

def get_data(file_name):
    rows = []
    data_file = open(file_name, 'r')
    reader = csv.reader(data_file)
    next(reader, None)
    
    for row in reader:
        rows.append(row)
    return rows

@ddt
class TestAvianca(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
    
    @data(*get_data('pom_avianca/avianca_data_base.csv'))
    @unpack
    def test_a_mainpage(self, departure_csv, departure_date_csv, destiny_csv, return_date_csv):
        main_page = AviancaMainPage(self.driver)
        main_page.open()
        main_page.book_fly(departure_csv, departure_date_csv, destiny_csv, return_date_csv)
    
    @classmethod    
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity = 2)