import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope='class')
def setup(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    wait = WebDriverWait(driver=driver, timeout=30)
    driver.get('https://yatra.com')
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.wait = wait


    yield

    driver.quit()