from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class TestResult:
    def test_footer(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://only.digital/')
        try:
            driver.find_element(By.XPATH, '//footer')
            print("Element found")
        except NoSuchElementException:
            print("No element found")

    def test_footer_project(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://only.digital/projects')
        try:
            driver.find_element(By.XPATH, '//footer')
            print("Element found")
        except NoSuchElementException:
            print("No element found")