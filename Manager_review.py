import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from Basepage import Basepage


class Manager(Basepage):
    manager = (By.XPATH, "(//span[normalize-space()='Manage Reviews'])[1]")
    manager_review = (By.XPATH,"(//a[normalize-space()='Manage Reviews'])[1]")
    type = (By.XPATH,"(//input[@placeholder='Type for hints...'])[1]")
    name = (By.XPATH,"(//span[contains(text(),'Peter Mac Anderson')])[1]")
    job_title = (By.XPATH, "//div[contains(text(),'-- Select --')][1]")
    job = (By.XPATH,"(//span[normalize-space()='Automaton Tester'])[1]")
    review_status = (By.XPATH,"(//div[@clear='false'])[1]")
    status = (By.XPATH,"//span[normalize-space()='Activated']")
    include = (By.XPATH,"(//div[contains(text(),'Current Employees Only')])[1]")
    select = (By.XPATH,"(//span[normalize-space()='Current and Past Employees'])[1]")
    reviewers = (By.XPATH,"(//input[@placeholder='Type for hints...'])[2]")
    names = (By.XPATH, "(//span[contains(text(),'Peter Mac Anderson')])[1]")
    from_date = (By.XPATH,"(//input[@placeholder='yyyy-dd-mm'])[1]")
    to_date = (By.XPATH,"(//input[@placeholder='yyyy-dd-mm'])[1]")
    search = (By.XPATH,"//button[normalize-space()='Search']")
    reset = (By.XPATH,"(//button[normalize-space()='Reset'])[1]")

    def __init__(self, driver):
        super().__init__(driver)


    def performance_manager(self, text, text1):
        self.hrm_btn_click(self.manager)
        self.hrm_btn_click(self.manager_review)
        self.hrm_sendkeys(self.type, text)
        time.sleep(5)
        self.hrm_btn_click(self.name)
        time.sleep(5)
        self.hrm_btn_click(self.job_title)
        time.sleep(5)
        self.hrm_btn_click(self.job)
        time.sleep(5)
        self.hrm_btn_click(self.review_status)
        time.sleep(5)
        self.hrm_btn_click(self.status)
        time.sleep(5)
        self.hrm_btn_click(self.include)
        time.sleep(5)
        self.hrm_btn_click(self.select)
        time.sleep(5)
        self.hrm_sendkeys(self.reviewers, text1)
        time.sleep(5)
        self.hrm_btn_click(self.names)
        time.sleep(5)
        self.hrm_btn_click(self.from_date)
        time.sleep(5)
        self.hrm_btn_click(self.to_date)
        time.sleep(5)
        self.hrm_btn_click(self.search)
        time.sleep(5)

        self.hrm_btn_click(self.reset)
        time.sleep(5)














