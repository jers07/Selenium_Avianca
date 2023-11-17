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
    
    def book_fly(self):
        #accept cookie
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'onetrust-accept-btn-handler')))
        accept_cookies_button = self._driver.find_element(By.ID, 'onetrust-accept-btn-handler')
        accept_cookies_button.click()
        
           
        
        
        
        
        #select departure airport
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="originDiv"]/input')))     
        origin_button = self._driver.find_element(By.ID, 'originBtn')
        origin_field = self._driver.find_element(By.XPATH, '//*[@id="originDiv"]/input')
        origin_button.click()
        origin_field.send_keys('cartagena') 
        origin_confirm = self._driver.find_element(By.XPATH, '//*[@id="departureStationsListId"]/li/button')
        origin_confirm.click()
        
        #select destiny airport
        destiny_field = self._driver.find_element(By.XPATH, '//*[@id="inputSearch"]/div[1]/station-control-custom/div/div[1]/div[2]/div[3]/div/input')
        destiny_field.send_keys('medellin')
        destiny_confirm = self._driver.find_element(By.XPATH, '//*[@id="arrivalStationsListId"]/li/button/span[2]')
        destiny_confirm.click()
        
        #select departure date
        next_button = self._driver.find_element(By.XPATH,'//*[@id="inputSearch"]/div[2]/date-control-custom/div/div[2]/div/div[2]/date-picker-custom/div/ngb-datepicker/div[1]/ngb-datepicker-navigation/div[2]/button')
        departure_date = self._driver.find_element(By.XPATH, '//div[@class="control_options ng-star-inserted"]/div[@class="control_options_inner"]/div[@class="control_options_scroll"]/date-picker-custom/div/ngb-datepicker/div[@class="ngb-dp-months"]/div[@class="ngb-dp-month ng-star-inserted"]/ngb-datepicker-month-view/div[@class="ngb-dp-week ng-star-inserted"]/div[@aria-label="7-11-2023"]')
        while True:
            counter = 0
            if counter > 11 or self._driver.find_element(By.XPATH,'//div[@class="control_options ng-star-inserted"]/div[@class="control_options_inner"]/div[@class="control_options_scroll"]/date-picker-custom/div/ngb-datepicker/div[@class="ngb-dp-months"]/div[@class="ngb-dp-month ng-star-inserted"]/ngb-datepicker-month-view/div[@class="ngb-dp-week ng-star-inserted"]/div[@aria-label="7-11-2023"]').is_enabled():
                break
            next_button.click()
            sleep(1)
            counter += 1
        departure_date.click()
        
        #return date
        next_button = self._driver.find_element(By.XPATH,'//*[@id="inputSearch"]/div[2]/date-control-custom/div/div[2]/div/div[2]/date-picker-custom/div/ngb-datepicker/div[1]/ngb-datepicker-navigation/div[2]/button')
        
        while True:
            counter = 0
            next_button.click()
            sleep(1)
            if counter > 11 or self._driver.find_element(By.XPATH,'//div[@class="control_options ng-star-inserted"]/div[@class="control_options_inner"]/div[@class="control_options_scroll"]/date-picker-custom/div/ngb-datepicker/div[@class="ngb-dp-months"]/div[@class="ngb-dp-month ng-star-inserted"]/ngb-datepicker-month-view/div[@class="ngb-dp-week ng-star-inserted"]/div[@aria-label="20-1-2024"]').is_enabled():
                break
            counter += 1
            
            
        return_date = self._driver.find_element(By.XPATH,'//div[@class="control_options ng-star-inserted"]/div[@class="control_options_inner"]/div[@class="control_options_scroll"]/date-picker-custom/div/ngb-datepicker/div[@class="ngb-dp-months"]/div[@class="ngb-dp-month ng-star-inserted"]/ngb-datepicker-month-view/div[@class="ngb-dp-week ng-star-inserted"]/div[@aria-label="20-1-2024"]')
        return_date.click()
        #sleep(1)
        
        #press search button
        search_button = self._driver.find_element(By.ID, 'searchButton')
        search_button.click()    
        
        #turn off direct fly
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="maincontent"]/div/div[2]/div/div/journey-availability-select-container/div/price-journey-select-custom/div[2]/div[1]/journey-filter-control-custom/div/ul/li[2]/div/label')))
        direct_fly_checkbox = self._driver.find_element(By.XPATH, '//*[@id="maincontent"]/div/div[2]/div/div/journey-availability-select-container/div/price-journey-select-custom/div[2]/div[1]/journey-filter-control-custom/div/ul/li[2]/div/label')
        direct_fly_checkbox.click()
        sleep(2)
        
        #select lowest price
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="filters-control_group filters-control_group--sortby"]/ul/li[@class="filters-control_list_item"]/div/label')))
        lowest_price_checkbox = self._driver.find_element(By.XPATH, '//div[@class="filters-control_group filters-control_group--sortby"]/ul/li[@class="filters-control_list_item"]/div/label')
        lowest_price_checkbox.click()
        sleep(1)
        
        #select departure fly
        cheapest_fly = self._driver.find_element(By.XPATH, '//*[@id="journeyFare_3433353434373745344434343435374533393335333633313745343135363745333233303332333332443331333132443330333737453335333333343335333433373332343433343331333533363333333933333335333333363333333133323434333433333335333433343337333434343334333433343335333234343333333233333330333333323333333333323434333333313333333133323434333333303333333733323434333333323333333033333332333333377E3331"]/journey-control-custom/div/div/div[1]/div[2]/button')
        cheapest_fly.click()
        sleep(1)
        cheapest_option = self._driver.find_element(By.XPATH, '//div[@class="journey_fares_list"]/div/fare-control/div[@class="fare-control fare5 cro-new-xs-button"]/div[@class="fare_footer"]/button')
        cheapest_option.click()
        sleep(1)
        confirm_cheapest = self._driver.find_element(By.XPATH, '//*[@id="FB310"]/div[3]/div[1]')
        sleep(1)
        confirm_cheapest.click()
        sleep(2)
        
        #turn off direct fly (departure case)
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="maincontent"]/div/div[2]/div/div/journey-availability-select-container/div/price-journey-select-custom/div[2]/div[1]/journey-filter-control-custom/div/ul/li[2]/div/label')))
        direct_fly_checkbox = self._driver.find_element(By.XPATH, '//*[@id="maincontent"]/div/div[2]/div/div/journey-availability-select-container/div/price-journey-select-custom/div[2]/div[1]/journey-filter-control-custom/div/ul/li[2]/div/label')
        direct_fly_checkbox.click()
        sleep(2)
        
        #select lowest price
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="filters-control_group filters-control_group--sortby"]/ul/li[@class="filters-control_list_item"]/div/label')))
        lowest_price_checkbox = self._driver.find_element(By.XPATH, '//div[@class="filters-control_group filters-control_group--sortby"]/ul/li[@class="filters-control_list_item"]/div/label')
        lowest_price_checkbox.click()
        sleep(1)
        
        #select return fly
        cheapest_fly_return = self._driver.find_element(By.XPATH,'//div[@id="journeyFare_3444343434353745343335343437374533393333333833363745343135363745333233303332333432443330333132443332333037453335333333343335333433373332343433343331333533363333333933333333333333383333333633323434333434343334333433343335333433333335333433343337333234343333333233333330333333323333333433323434333333303333333133323434333333323333333033323434333333323333333133333332333333367E3331"]/journey-control-custom/div/div/div[@class="journey_inner"]/div[@class="journey_price"]/button')
        cheapest_fly_return.click()
        sleep(2)
        urgency_message_button = self._driver.find_element(By.XPATH, '//*[@id="bx-close-icon"]')
        urgency_message_button.click()
        sleep(1)
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
        accept_button.click()
        