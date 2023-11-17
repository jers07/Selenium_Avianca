import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import select
from time import sleep

class AviancaMainPage(object):
    def __init__(self, driver):
        self._driver = driver
        self._url = 'https://www.avianca.com/es/'
        
    def open(self):
        self._driver.get(self._url)
        self._driver.maximize_window()
        sleep(1)
    
    def book_fly(self, departure_csv, departure_date_csv, destiny_csv, return_date_csv):
        #accept cookie
        try:
            WebDriverWait(self._driver, 5).until(EC.presence_of_element_located((By.ID, 'onetrust-accept-btn-handler')))
            accept_cookies_button = self._driver.find_element(By.ID, 'onetrust-accept-btn-handler')
            accept_cookies_button.click()
        except Exception as e:
            print('it never appears')
        
        #select departure airport
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="originDiv"]/input')))     
        origin_button = self._driver.find_element(By.ID, 'originBtn')
        origin_field = self._driver.find_element(By.XPATH, '//*[@id="originDiv"]/input')
        origin_button.click()
        origin_field.send_keys(departure_csv) 
        origin_confirm = self._driver.find_element(By.XPATH, '//*[@id="departureStationsListId"]/li/button')
        origin_confirm.click()
        
        #select destiny airport
        destiny_field = self._driver.find_element(By.XPATH, '//*[@id="inputSearch"]/div[1]/station-control-custom/div/div[1]/div[2]/div[3]/div/input')
        destiny_field.send_keys(destiny_csv)
        destiny_confirm = self._driver.find_element(By.XPATH, '//*[@id="arrivalStationsListId"]/li/button/span[2]')
        destiny_confirm.click()
        
        #select departure date
        next_button = self._driver.find_element(By.XPATH,'//*[@id="inputSearch"]/div[2]/date-control-custom/div/div[2]/div/div[2]/date-picker-custom/div/ngb-datepicker/div[1]/ngb-datepicker-navigation/div[2]/button')
        previous_button = self._driver.find_element(By.XPATH, '//ngb-datepicker-navigation/div[@class="ngb-dp-arrow"]/button')
        for i in range(24):
            try:
                departure_date_check = self._driver.find_element(By.XPATH,(f'(//div[@class="control_options ng-star-inserted"]/div[@class="control_options_inner"]/div[@class="control_options_scroll"]/date-picker-custom/div/ngb-datepicker/div[@class="ngb-dp-months"]/div[@class="ngb-dp-month ng-star-inserted"]/ngb-datepicker-month-view/div[@class="ngb-dp-week ng-star-inserted"]/div[@aria-label="{departure_date_csv}"])[1]'))
                departure_date_check.click()
                break   
                 
            except Exception as e:
                try:
                    next_button.click()
                except Exception as e:
                    for i in range(10):
                        previous_button.click()
                
        #return date
        next_button = self._driver.find_element(By.XPATH,'//*[@id="inputSearch"]/div[2]/date-control-custom/div/div[2]/div/div[2]/date-picker-custom/div/ngb-datepicker/div[1]/ngb-datepicker-navigation/div[2]/button')

        for i in range(12):
            try:
                return_date = self._driver.find_element(By.XPATH,f'(//div[@class="control_options ng-star-inserted"]/div[@class="control_options_inner"]/div[@class="control_options_scroll"]/date-picker-custom/div/ngb-datepicker/div[@class="ngb-dp-months"]/div[@class="ngb-dp-month ng-star-inserted"]/ngb-datepicker-month-view/div[@class="ngb-dp-week ng-star-inserted"]/div[@aria-label="{return_date_csv}"])[1]')
                return_date.click()
                break 
            except Exception as e:
                sleep(1)
                next_button.click()
                     
        #press search button
        search_button = self._driver.find_element(By.ID, 'searchButton')
        search_button.click()    
        
        #turn off direct flight
        try:
            WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="maincontent"]/div/div[2]/div/div/journey-availability-select-container/div/price-journey-select-custom/div[2]/div[1]/journey-filter-control-custom/div/ul/li[2]/div/label')))
            direct_fly_checkbox = self._driver.find_element(By.XPATH, '//*[@id="maincontent"]/div/div[2]/div/div/journey-availability-select-container/div/price-journey-select-custom/div[2]/div[1]/journey-filter-control-custom/div/ul/li[2]/div/label')
            sleep(2)
            direct_fly_checkbox.click()
        except Exception as e:
            print('no departure direct fly')
        
        #select lowest price
        try:
            WebDriverWait(self._driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="filters-control_group filters-control_group--sortby"]/ul/li[@class="filters-control_list_item"]/div/label')))
            lowest_price_checkbox = self._driver.find_element(By.XPATH, '//div[@class="filters-control_group filters-control_group--sortby"]/ul/li[@class="filters-control_list_item"]/div/label')
            lowest_price_checkbox.click()
            sleep(1)
        except Exception as e:
            print('no cheap departure flight for you')
        
        #select departure flight
        
        cheapest_fly = self._driver.find_element(By.XPATH, '//div[@class="journey-selector journey-selector-outbound ng-star-inserted"]/price-journey-select-custom/div[@class="journey-select_container"]/div[@class="journey-select_list ng-star-inserted FB310"]/div[@class="journey-select_list_item ng-star-inserted FB293"]')
        cheapest_fly.click()
        sleep(1)
        cheapest_option = self._driver.find_element(By.XPATH, '//div[@class="journey_fares_list"]/div/fare-control/div[@class="fare-control fare5 cro-new-xs-button"]/div[@class="fare_footer"]/button')
        cheapest_option.click()
        sleep(1)
        confirm_cheapest = self._driver.find_element(By.XPATH, '//*[@id="FB310"]/div[3]/div[1]')
        sleep(1)
        confirm_cheapest.click()
        sleep(2)
        
        #turn off direct flight (return case)
        try:
            WebDriverWait(self._driver, 8).until(EC.presence_of_element_located((By.XPATH, '//*[@id="maincontent"]/div/div[2]/div/div/journey-availability-select-container/div/price-journey-select-custom/div[2]/div[1]/journey-filter-control-custom/div/ul/li[2]/div/label')))
            direct_fly_checkbox = self._driver.find_element(By.XPATH, '//*[@id="maincontent"]/div/div[2]/div/div/journey-availability-select-container/div/price-journey-select-custom/div[2]/div[1]/journey-filter-control-custom/div/ul/li[2]/div/label')
            sleep(2)
            direct_fly_checkbox.click()
        except Exception as e:
            print('no return direct fly option')
        
        #select lowest price
        try:
            if self._driver.find_element(By.XPATH, '//*[@id="maincontent"]/div/div[2]/div/div/journey-availability-select-container/div/price-journey-select-custom/div[2]/div[1]/journey-filter-control-custom/div/ul/li[2]/div/label').is_enabled():
                WebDriverWait(self._driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="filters-control_group filters-control_group--sortby"]/ul/li[@class="filters-control_list_item"]/div/label')))
                lowest_price_checkbox = self._driver.find_element(By.XPATH, '//div[@class="filters-control_group filters-control_group--sortby"]/ul/li[@class="filters-control_list_item"]/div/label')
                lowest_price_checkbox.click()
                sleep(1)
        except Exception as e:
            print('no return lowest price option')
            sleep(2)
        
        #select return flight
        cheapest_fly_return = self._driver.find_element(By.XPATH,'((//div[@class="journey-select_list ng-star-inserted FB310"])[2]/div[@class="journey-select_list_item ng-star-inserted FB293"]/journey-control-custom/div/div/div/div[@class="journey_price"]/button)[1]')
        cheapest_fly_return.click()
   
        
        try:
            urgency_message_button = self._driver.find_element(By.XPATH, '//*[@id="bx-close-icon"]')
            sleep(1)
            urgency_message_button.click()
        except Exception as e:
            print('no urgency message')

        WebDriverWait(self._driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="journey_fares_list"]/div/fare-control/div[@class="fare-control fare5 cro-new-xs-button"]/div[@class="fare_footer"]/button')))
        cheapest_option_return = self._driver.find_element(By.XPATH, '//div[@class="journey_fares_list"]/div/fare-control/div[@class="fare-control fare5 cro-new-xs-button"]/div[@class="fare_footer"]/button')
        cheapest_option_return.click()
        sleep(1)
        
        
        confirm_cheapest_return = self._driver.find_element(By.XPATH, '//*[@id="FB310"]/div[3]/div[1]')
        sleep(1)
        confirm_cheapest_return.click()
        sleep(2)
        
        #confirm flight
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH,'//div[@class="page_buttons_wrapper ng-star-inserted"]/div/button')))
        accept_button = self._driver.find_element(By.XPATH,'//div[@class="page_buttons_wrapper ng-star-inserted"]/div/button')
        sleep(1)
        accept_button.click()
        sleep(2)
        
        