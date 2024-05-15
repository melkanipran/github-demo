import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver

class LaunchPage(BaseDriver):

    FROM_LOCATION_FIELD = "//input[@id='BE_flight_origin_city']"
    FROM_LOCATION_LIST = "//*[@class='ac_airport']"
    TO_LOCATION_FIELD = "//input[@id='BE_flight_arrival_city']"
    TO_LOCATION_LIST = "//*[@class='ac_airport']"
    DEPARTURE_DATE_FIELD = "//input[@id='BE_flight_origin_date']"
    DEPARTURE_DATE_LIST = "//div[@id='monthWrapper']//table//tbody//tr//td[@class!='inActiveTD' and @class!='inActiveTD weekend']"
    SEARCH_BTN = "//input[@id='BE_flight_flsearch_btn' and @value='Search Flights']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    def getFromLocationField(self):
        return self.driver.find_element(By.XPATH, self.FROM_LOCATION_FIELD)
    
    def getFromLocationList(self):
        return self.driver.find_elements(By.XPATH, self.FROM_LOCATION_LIST)
    
    def getToLocationField(self):
        return self.driver.find_element(By.XPATH, self.TO_LOCATION_FIELD)

    def getToLocationList(self):
        return self.driver.find_elements(By.XPATH, self.TO_LOCATION_LIST)
    
    def getDepartureDateField(self):
        return self.driver.find_element(By.XPATH, self.DEPARTURE_DATE_FIELD)
    
    def getDepartureDateList(self):
        return self.driver.find_elements(By.XPATH, self.DEPARTURE_DATE_LIST)
    
    def getSearchBtn(self):
        return self.driver.find_element(By.XPATH, self.SEARCH_BTN)
    
    def enterFromLocation(self, from_place):
        self.element_to_be_clickable(self.FROM_LOCATION_FIELD)
        from_loc_field = self.getFromLocationField()
        from_loc_field.click()
        time.sleep(1)
        from_loc_field.send_keys(from_place)
        time.sleep(1)
        location_list = self.getFromLocationList()
        for from_location in location_list:
            print(from_location.text.upper())
            print(from_place in from_location.text.upper())
            print("(GOX)" in from_location.text.upper())
            if "(GOX)" in from_location.text.upper():
                from_location.click()
                break
            print("***")
            time.sleep(1)
    
    def enterToLocation(self, to_place):
        self.element_to_be_clickable(self.TO_LOCATION_FIELD)
        to_location = self.getToLocationField()
        to_location.click()
        time.sleep(1)
        to_location.send_keys(to_place)
        time.sleep(1)
        to_location.send_keys(Keys.RETURN)
        # location_list = self.getToLocationList()
        # for location in location_list:
        #     if to_place in location_list and "(DEL)" in location.text:
        #         location.click()
        #         break

    def selectDepartureDate(self, departure_date):
        self.element_to_be_clickable(self.DEPARTURE_DATE_FIELD)
        departure_date_field = self.getDepartureDateField()
        departure_date_field.click()
        time.sleep(1)
        # self.element_to_be_clickable(self.DEPARTURE_DATE_LIST)
        self.visibility_of_all_elements(self.DEPARTURE_DATE_LIST)
        date_list = self.getDepartureDateList()
        print(len(date_list))
        for date in date_list:
            if date.get_attribute('id') == departure_date:
                date.click()
                break
    
    def clickSearchBtn(self):
        self.element_to_be_clickable(self.SEARCH_BTN)
        search_btn = self.getSearchBtn()
        search_btn.click()

    def searchFlights(self, from_place, to_place, departure_date):
        self.enterFromLocation(from_place)
        self.enterToLocation(to_place)
        self.selectDepartureDate(departure_date)
        self.clickSearchBtn()
