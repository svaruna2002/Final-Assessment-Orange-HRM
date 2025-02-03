import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from Basepage import Basepage


class Employee(Basepage):
    manager = (By.XPATH,"(//span[normalize-space()='Manage Reviews'])[1]")
    emp = (By.XPATH,"(//a[normalize-space()='Employee Reviews'])[1]")
    emp_name = (By.XPATH,"(//input[@placeholder='Type for hints...'])[1]")
    name = (By.XPATH,"(//span[contains(text(),'Peter Mac Anderson')])[1]")
    job_title = (By.XPATH,"(//div[@class='oxd-select-text-input'][normalize-space()='-- Select --'])[1]")
    job = (By.XPATH,"(//span[normalize-space()='Automaton Tester'])[1]")
    sub_unit = (By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]")
    unit = (By.XPATH,"//span[normalize-space()='Engineering']")
    include = (By.XPATH,"(//div[contains(text(),'Current Employees Only')])[1]")
    inc = (By.XPATH,"//span[normalize-space()='Current and Past Employees']")
    review_status = (By.XPATH,"(//div[contains(text(),'-- Select --')])[1]")
    status = (By.XPATH,"//span[normalize-space()='In Progress']")
    from_date = (By.XPATH,"(//input[@placeholder='yyyy-dd-mm'])[1]")
    to_date = (By.XPATH,"(//input[@placeholder='yyyy-dd-mm'])[2]")
    search = (By.XPATH,"//button[normalize-space()='Search']")
    reset = (By.XPATH,"//button[normalize-space()='Reset']")

    def __init__(self, driver):
        super().__init__(driver)

    def performance_employee(self):
        self.hrm_btn_click(self.manager)
        self.hrm_btn_click(self.emp)

    def performance_empl(self, txt):
        self.hrm_sendkeys(self.emp_name, txt)
        time.sleep(3)
        self.hrm_btn_click(self.name)
        time.sleep(3)
        self.hrm_btn_click(self.job_title)
        time.sleep(3)
        self.hrm_btn_click(self.job)
        time.sleep(3)
        self.hrm_btn_click(self.sub_unit)
        time.sleep(3)
        self.hrm_btn_click(self.unit)
        time.sleep(3)
        self.hrm_btn_click(self.include)
        time.sleep(3)
        self.hrm_btn_click(self.inc)
        time.sleep(3)
        self.hrm_btn_click(self.review_status)
        time.sleep(3)
        self.hrm_btn_click(self.status)
        time.sleep(3)
        self.hrm_btn_click(self.from_date)
        time.sleep(3)
        self.hrm_btn_click(self.to_date)
        time.sleep(3)
        self.hrm_btn_click(self.search)
        time.sleep(3)
        self.hrm_btn_click(self.reset)


