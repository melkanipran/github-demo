from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseDriver():
    def __init__(self, driver):
        self.driver = driver

    def scrollPage(self):
        footer = self.driver.find_element(By.XPATH, "//*[@class='yatraSecure']");
        flag = self.driver.execute_script("""var myElement = arguments[0]; var bounding = myElement.getBoundingClientRect();
                    if (bounding.top >= 0 && bounding.left >= 0 && bounding.right <= window.innerWidth && bounding.bottom <= window.innerHeight) { return true;} else {return false;}""", footer)
        print(flag)

        while(flag == False):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            flag = self.driver.execute_script("""var myElement = arguments[0]; var bounding = myElement.getBoundingClientRect();
                    if (bounding.top >= 0 && bounding.left >= 0 && bounding.right <= window.innerWidth && bounding.bottom <= window.innerHeight) { return true;} else {return false;}""", footer)
    
    def element_to_be_clickable(self, xpath):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

    def visibility_of_all_elements(self, xpath):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.visibility_of_all_elements_located((By.XPATH, xpath)))