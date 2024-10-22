import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()    # Для Selenium
def set_up_browser():
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(60)
    driver.maximize_window()
    yield driver
    driver.quit()


