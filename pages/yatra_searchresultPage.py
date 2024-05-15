import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver

class SearchResults(BaseDriver):
    ONE_FLIGHT_FILTER_DIV = "//div[contains(@class, 'filter-stops')]//label//p[text()='1']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    def getOneFlightFilterDiv(self):
        return self.driver.find_element(By.XPATH, self.ONE_FLIGHT_FILTER_DIV)

    def filterOneFlight(self):
        self.element_to_be_clickable(self.ONE_FLIGHT_FILTER_DIV)
        one_stop = self.getOneFlightFilterDiv()
        one_stop.click()

    # def filterOneFlight(self):
    #     self.element_to_be_clickable("//div[contains(@class, 'filter-stops')]//label//p[text()='1']")
    #     one_stop = self.driver.find_element(By.XPATH, "//div[contains(@class, 'filter-stops')]//label//p[text()='1']")
    #     one_stop.click()

        