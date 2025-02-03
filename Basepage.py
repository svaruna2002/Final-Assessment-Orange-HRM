# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class Basepage:
#     def __init__(self, driver):
#         self.driver = driver
#
#     def hrm_btn_click(self, locator):
#         WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(locator)).click()
#
#     def hrm_sendkeys(self, locator, text):
#         WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator)).send_keys(text)
#
#     def wait_for_element(self,locator):
#         WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(locator)).click()

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Basepage:
    def __init__(self, driver):
        self.driver = driver

    def hrm_btn_click(self, locator):
        try:
            element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            raise Exception(f"Timeout while waiting for element {locator} to be clickable")

    def hrm_sendkeys(self, locator, text):
        try:
            element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))
            element.send_keys(text)
        except TimeoutException:
            raise Exception(f"Timeout while waiting for element {locator} to be visible")

    def wait_for_element(self, locator):
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise Exception(f"Timeout while waiting for element {locator} to be present")

    def scroll(self, locator):
        element = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
