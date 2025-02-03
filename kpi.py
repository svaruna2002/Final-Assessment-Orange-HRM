import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Basepage import Basepage


class Kpi(Basepage):
    select = (By.XPATH, "//div[@class='oxd-select-text-input']")
    perf = (By.LINK_TEXT, "Performance")
    config = (By.XPATH, "//span[normalize-space()='Configure']//i[@class='oxd-icon bi-chevron-down']")
    kpi = (By.XPATH, "//a[@class='oxd-topbar-body-nav-tab-link'][1]")
    a = (By.XPATH, "//span[text()='HR Manager']")
    search = (By.XPATH, "//button[@type='submit']")
    b = (By.CSS_SELECTOR, "[type='button']")
    # checkbox = (By.CSS_SELECTOR, "div[role='columnheader'] i[class='oxd-icon bi-check oxd-checkbox-input-icon']")
    checkbox = (By.XPATH, "(//div[@class='oxd-table-card-cell-checkbox'])[4]")
    delete = (By.XPATH, "(//button[normalize-space()='Delete Selected'])[1]")
    dele = (By.CSS_SELECTOR,"button[class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin']" )
    # dele1 = (By.XPATH, "(//button[normalize-space()='Delete Selected'])[1]")
    can = (By.XPATH, "//button[normalize-space()='No, Cancel']")
    reset = (By.CSS_SELECTOR, "button[type='reset']")
    trash = (By.XPATH, "(//i[@class='oxd-icon bi-trash'])[1]")
    yes_delete = (By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin']")
    trash_1 = (By.XPATH, "(//i[@class='oxd-icon bi-trash'])[1]")
    no_delete = (By.XPATH, "//button[normalize-space()='No, Cancel']")
    pencil = (By.XPATH, "(//i[@class='oxd-icon bi-pencil-fill'])[1]")
    edit_kpi = (By.XPATH, "//div[@class='oxd-select-text-input']")
    job_title = (By.XPATH, "//span[normalize-space()='Automaton Tester']")
    min_rating = (By.XPATH, "(//input[@modelmodifiers='[object Object]'])[1]")
    max_rating = (By.XPATH, "(//input[@modelmodifiers='[object Object]'])[2]")
    switch = (By.XPATH, "(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[1]")
    save = (By.CSS_SELECTOR, "button[type='submit']")
    add = (By.XPATH, "//button[normalize-space()='Add']")
    c = (By.XPATH, "//button[normalize-space()='Add']")
    pencil1 = (By.XPATH, "(//i[@class='oxd-icon bi-pencil-fill'])[2]")
    addddddd = (By.XPATH, "//button[normalize-space()='Add']")
    cancel1 = (By.XPATH, "//button[normalize-space()='Cancel']")
    add1 = (By.XPATH, "//button[normalize-space()='Add']")
    key = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
    job_title1 = (By.CSS_SELECTOR, ".oxd-select-text-input")
    job = (By.XPATH, "(//span[normalize-space()='Chief Executive Officer'])[1]")
    min = (By.XPATH, "(//input[@modelmodifiers='[object Object]'])[1]")
    switch1 = (By.XPATH, "(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[1]")
    save1 = (By.CSS_SELECTOR, "button[type='submit']")
    add2 = (By.XPATH, "//button[normalize-space()='Add']")
    kpi1 = (By.CSS_SELECTOR, "div[class='oxd-grid-2 orangehrm-full-width-grid'] div[class='oxd-grid-item oxd-grid-item--gutters'] div[class='oxd-input-group oxd-input-field-bottom-space'] div input[class='oxd-input oxd-input--active']")
    job_title2 = (By.CSS_SELECTOR, ".oxd-select-text-input")
    job2 = (By.XPATH, "(//span[normalize-space()='Chief Executive Officer'])[1]")
    rate = (By.XPATH, "(//input[@modelmodifiers='[object Object]'])[1]")
    switch3 = (By.XPATH, "(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[1]")
    cancel3 = (By.XPATH, "//button[normalize-space()='Cancel']")

    def __init__(self, driver):
        super().__init__(driver)

    def performance_kpi(self):
        try:
            self.hrm_btn_click(self.perf)
            self.hrm_btn_click(self.config)
            self.hrm_btn_click(self.kpi)
        except Exception as e:
            print(f"Error navigating to Performance KPI: {e}")
            raise

    def key_performance(self):
        self.hrm_btn_click(self.select)
        time.sleep(5)
        self.hrm_btn_click(self.a)
        time.sleep(5)
        self.hrm_btn_click(self.search)
        self.hrm_btn_click(self.reset)
        time.sleep(6)
        self.hrm_btn_click(self.checkbox)
        time.sleep(6)

        # checkbox = self.wait_for_element(self.checkbox)
        # self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkbox)
        # check = self.wait_for_element(self.b)
        # self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", self.check)


    def checkbox_performance(self):
        self.hrm_btn_click(self.delete)
        time.sleep(5)
        self.hrm_btn_click(self.dele)
        time.sleep(5)
        # self.scroll(self.addddddd)
        self.hrm_btn_click(self.checkbox)
        time.sleep(5)

        self.hrm_btn_click(self.delete)
        time.sleep(5)
        self.hrm_btn_click(self.can)

    def delete_performance(self):
        self.hrm_btn_click(self.reset)
        time.sleep(5)
        self.hrm_btn_click(self.trash)
        time.sleep(5)

        self.hrm_btn_click(self.yes_delete)
        time.sleep(5)

        self.hrm_btn_click(self.trash_1)
        time.sleep(5)

        self.hrm_btn_click(self.no_delete)

    def edit_perfformance(self,text, minval):
        self.hrm_btn_click(self.pencil)
        time.sleep(5)
        self.hrm_sendkeys(self.edit_kpi,text)
        time.sleep(5)

        self.hrm_btn_click(self.job_title)
        time.sleep(5)

        self.hrm_sendkeys(self.min_rating,minval)
        time.sleep(5)

        # self.hrm_sendkeys(self.max_rating, maxval)
        time.sleep(5)

        self.hrm_btn_click(self.switch)
        time.sleep(5)

        self.hrm_btn_click(self.save)
        time.sleep(5)

        self.scroll(self.add)
        time.sleep(5)

        self.hrm_btn_click(self.pencil1)
        time.sleep(5)

        self.hrm_btn_click(self.cancel1)

    def add_performance(self, txt):
        self.hrm_btn_click(self.add1)
        self.hrm_sendkeys(self.key,txt)
        time.sleep(4)
        self.hrm_btn_click(self.job_title1)
        self.hrm_btn_click(self.job)
        time.sleep(5)
        # bty = self.hrm_btn_click(min)
        # bty.send_keys(Keys.CONTROL, 'a')
        # bty.send_keys(Keys.BACKSPACE)
        # time.sleep(3)
        # self.hrm_sendkeys(self.min, min_value)
        # time.sleep(3)
        # actions = ActionChains(self.driver)
        # actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
        # self.hrm_sendkeys(self.min, min_value)
        self.hrm_btn_click(self. switch1)
        self.hrm_btn_click(self.save1)
        self.hrm_btn_click(self.add1)






