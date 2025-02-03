import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class Dashboard:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 13)  # Wait up to 13 seconds for elements to appear

    def wait_for_element(self, locator):
        """Wait for an element to be visible and return it."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def navigate_to_performance_page(self):
        """Navigate to the Performance page."""
        self.driver.find_element(By.LINK_TEXT, "Performance").click()
        time.sleep(3)

    def navigate_to_employee_tracker(self):
        """Navigate to the Employee Tracker page."""
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Employee Trackers']").click()
        time.sleep(3)

    def select_employee(self, employee_name):
        """Search for and select an employee."""
        self.driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']").send_keys(employee_name)
        time.sleep(3)
        self.driver.find_element(By.XPATH, f"//span[normalize-space()='{employee_name}']").click()
        time.sleep(3)

    def change_include_option(self, option_text):
        """Change the include filter option."""
        self.driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, f"//span[normalize-space()='{option_text}']").click()
        time.sleep(3)

    def search_and_reset(self):
        """Perform a search and reset the filters."""
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='reset']").click()
        time.sleep(2)

    def add_log(self, log_text, review_type, comment):
        self.driver.find_element(By.XPATH, "(//button[@name='view'][normalize-space()='View'])[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Add Log']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Type here']").send_keys(log_text)
        time.sleep(2)
        self.driver.find_element(By.XPATH, f"//button[normalize-space()='{review_type}']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//textarea[@placeholder='Type here']").send_keys(comment)
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(3)

    def navigate_to_my_tracker_page(self):
        """Navigate to the My Tracker page."""
        self.driver.find_element(By.XPATH, "//a[normalize-space()='My Trackers']").click()
        time.sleep(3)

    def view_log(self):
        """Click on the view button."""
        self.driver.find_element(By.CSS_SELECTOR, "button[name='view']").click()
        time.sleep(3)

    def add_log_to_my_tracker(self, log_text, review_type, comment):
        """Add a log entry in the My Tracker page."""
        add_log_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add Log']"))
        )
        add_log_button.click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Type here']").send_keys(log_text)
        time.sleep(2)
        self.driver.find_element(By.XPATH, f"//button[normalize-space()='{review_type}']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//textarea[@placeholder='Type here']").send_keys(comment)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
        time.sleep(3)
