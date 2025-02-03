from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import time

class TestEmpTracker:
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Login']")
    PERFORMANCE_LINK = (By.LINK_TEXT, "Performance")
    EMPLOYEE_TRACKERS_LINK = (By.XPATH, "//a[normalize-space()='Employee Trackers']")
    EMPLOYEE_NAME_INPUT = (By.XPATH, "//input[@placeholder='Type for hints...']")
    SELECT_EMPLOYEE = (By.XPATH, "//span[normalize-space()='Peter Mac Anderson']")
    INCLUDE_DROPDOWN = (By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']")
    PAST_EMPLOYEES_ONLY_OPTION = (By.XPATH, "//span[normalize-space()='Past Employees Only']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    RESET_BUTTON = (By.CSS_SELECTOR, "button[type='reset']")
    VIEW_BUTTON = (By.CSS_SELECTOR, "button[name='view']")
    ADD_LOG_BUTTON = (By.XPATH, "//button[normalize-space()='Add Log']")
    LOG_INPUT = (By.XPATH, "//input[@placeholder='Type here']")
    POSITIVE_REVIEW_BUTTON = (By.XPATH, "//button[normalize-space()='Positive']")
    NEGATIVE_REVIEW_BUTTON = (By.XPATH, "//button[normalize-space()='Negative']")
    COMMENT_INPUT = (By.XPATH, "//textarea[@placeholder='Type here']")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    CANCEL_BUTTON = (By.XPATH, "//button[normalize-space()='Cancel']")
    MY_TRACKERS_LINK = (By.XPATH, "//a[normalize-space()='My Trackers']")
    SAVE_MY_TRACKER_BUTTON = (By.XPATH, "//button[normalize-space()='Save']")

    # login - username, password and submit button
    def login(self, driver):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(self.USERNAME_FIELD)).send_keys("Admin")
        time.sleep(4)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(self.PASSWORD_FIELD)).send_keys("admin123")
        time.sleep(4)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()
        time.sleep(4)

     # moving to performance page
    def navigate_to_performance(self, driver):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.PERFORMANCE_LINK)).click()
        time.sleep(4)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.EMPLOYEE_TRACKERS_LINK)).click()
        time.sleep(4)

    # searching employee name in Employee Tracker
    def search_employee(self, driver):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(self.EMPLOYEE_NAME_INPUT)).send_keys("Peter")
        time.sleep(4)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.SELECT_EMPLOYEE)).click()
        time.sleep(4)

     #selecting an option from include dropdown
    def include_dropdown(self,driver):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.INCLUDE_DROPDOWN)).click()
        time.sleep(4)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.PAST_EMPLOYEES_ONLY_OPTION)).click()
        time.sleep(4)

      #Employee Tracker Buttons
      # Employee Tracker search button
    def emp_tracker_search(self,driver):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.SEARCH_BUTTON)).click()
        time.sleep(4)

      #Employee Tracker Reset Button
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.RESET_BUTTON)).click()
        time.sleep(4)

      #Employee Tracker view button
    def view_employee(self, driver):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.VIEW_BUTTON)).click()
        time.sleep(4)

    # Employee Tracker add log button
    def add_log(self, driver):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.ADD_LOG_BUTTON)).click()
        time.sleep(4)

    # Employee Tracker log inputs
    def add_log_inputs(self, driver):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(self.LOG_INPUT)).send_keys("Agility")
        time.sleep(4)

    def emp_tracker_log_review(self,driver):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.POSITIVE_REVIEW_BUTTON)).click()
        time.sleep(4)

    def emp_tracker_log_comment(self,driver):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(self.COMMENT_INPUT)).send_keys("Finish the work")
        time.sleep(4)

    # employee review log save button
    def save_log(self, driver):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()
        time.sleep(4)

     # navigating to tracker page
    def navigate_to_my_trackers(self, driver):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.MY_TRACKERS_LINK)).click()
        time.sleep(4)

     # view button in tracker page
    def tracker_view_btn(self, driver):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.VIEW_BUTTON)).click()
        time.sleep(4)

     # adding a log in tracker page
    def add_new_tracker_log(self, driver):

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.ADD_LOG_BUTTON)).click()
        time.sleep(4)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(self.LOG_INPUT)).send_keys("Time Management")
        time.sleep(4)

    def tracker_log_review_icon(self,driver):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.NEGATIVE_REVIEW_BUTTON)).click()
        time.sleep(4)

    def tracker_log_comment(self,driver):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(self.COMMENT_INPUT)).send_keys("Good Job")
        time.sleep(4)

        # cancel button in log in tracker page
    def tracker_log_cancel(self,driver):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.CANCEL_BUTTON)).click()
        time.sleep(4)

    def test_employee_tracker(self, browser):
        driver = browser
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.login(driver)
        self.navigate_to_performance(driver)
        self.search_employee(driver)
        self.include_dropdown(driver)
        self.emp_tracker_search(driver)
        self.view_employee(driver)
        self.add_log(driver)
        self.add_log_inputs(driver)
        self.emp_tracker_log_review(driver)
        self.emp_tracker_log_comment(driver)
        self.save_log(driver)

    def test_my_tracker_page(self, browser):
        driver = browser
        self.navigate_to_my_trackers(driver)
        self.tracker_view_btn(driver)
        self.add_new_tracker_log(driver)
        self.tracker_log_review_icon(driver)
        self.tracker_log_comment(driver)
        self.tracker_log_cancel(driver)

