import time, pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.yatra_launchPage import LaunchPage
from pages.yatra_searchresultPage import SearchResults
from utilities.utils import Utils

@pytest.mark.usefixtures("setup")
class TestFlights():
    def test_flightDetails(self):
    
        # Search Flights
        lp = LaunchPage(self.driver)
        lp.searchFlights("Goa", "New Delhi", "10-05-2024")


        # select one flight
        sr = SearchResults(self.driver)
        sr.filterOneFlight()
        time.sleep(3)
        # sr.scrollPage()
            
        flight_list = self.driver.find_elements(By.XPATH, "//span[@class='dotted-borderbtm']")
        print(len(flight_list))

        ut = Utils()
        ut.assert_list_values(flight_list,"1 Stop")
        time.sleep(5)

