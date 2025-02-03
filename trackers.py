import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from Basepage import Basepage


class Trackers(Basepage):
    config = (By.XPATH,"//span[normalize-space()='Configure']//i[@class='oxd-icon bi-chevron-down']")
    tracker = (By.XPATH, "//a[normalize-space()='Trackers']")
    type = (By.XPATH, "//input[@placeholder='Type for hints...']")
    hints =(By.XPATH,"//span[normalize-space()='Peter Mac Anderson']")
    search = (By.CSS_SELECTOR,"button[type='submit']")
    reset = (By.XPATH, "//button[normalize-space()='Reset']")
    addddd = (By.XPATH,"(//button[normalize-space()='Add'])[1]")
    # checkbox = (By.XPATH, "//div[@role='table']//div[1]//div[1]//div[1]//div[1]//div[1]//label[1]")
    # delete = (By.XPATH, "(//button[normalize-space()='Delete Selected'])[1]")
    # dele1 = (By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin']")
    # checkbox1 = (By.XPATH, "(//i[@class='oxd-icon bi-check oxd-checkbox-input-icon'])[2]")
    # dele2 = (By.XPATH, "(//button[normalize-space()='Delete Selected'])[1]")
    # no_cancel = (By.XPATH, "//button[normalize-space()='No, Cancel']")
    trash = (By.XPATH, "//i[@class='oxd-icon bi-trash']")
    yes_delete = (By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin']")
    trash1 = (By.XPATH, "(//i[@class='oxd-icon bi-trash'])[2]")
    no_delete2 = (By.XPATH, "//button[normalize-space()='No, Cancel']")
    trash2 = (By.XPATH, "(//i[@class='oxd-icon bi-trash'])[2]")
    close = (By.XPATH, "//button[normalize-space()='×']")

    pencil = (By.XPATH, "(//button[@type='button'])[8]")
    tracker_name = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
    emp_name = (By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")
    name = (By.XPATH,"//span[contains(text(),'Peter Mac Anderson')]")
    # element = (By.XPATH, "(//i[@class='oxd-icon bi-x --clear'])[2]")
    reviewer = (By.XPATH,"(//input[@placeholder='Type for hints...'])[2]")
    name1 = (By.XPATH,"//span[contains(text(),'James')]")
    save = (By.CSS_SELECTOR, "button[type='submit']")

    addd = (By.XPATH, "//button[normalize-space()='Add']")
    pen = (By.XPATH, "(//i[@class='oxd-icon bi-pencil-fill'])[2]")
    canc = (By.XPATH, "//button[normalize-space()='Cancel']")

    add = (By.XPATH,"//button[normalize-space()='Add']")
    tracker_name1 = (By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")
    emp_name1 = (By.XPATH,"(//input[@placeholder='Type for hints...'])[1]")
    names = (By.XPATH,"//span[contains(text(),'Thomas Kutty Benny')]")
    reviewers = (By.XPATH,"(//input[@placeholder='Type for hints...'])[2]")
    name12 = (By.XPATH,"(//span[contains(text(),'Timothy Lewis Amiano')])")
    saves = (By.XPATH,"//button[normalize-space()='Save']")

    add1 = (By.XPATH,"//button[normalize-space()='Add']")
    cancel = (By.XPATH,"//button[normalize-space()='Cancel']")
    scr = (By.XPATH,"//button[normalize-space()='Add']")
    a = ("arguments[0].scrollIntoView(true);",scr)


    def __init__(self, driver):
        super().__init__(driver)

    def performance_tracker(self):
        self.hrm_btn_click(self.config)
        self.hrm_btn_click(self.tracker)

    def tracker_search(self, text):
        time.sleep(3)
        self.hrm_sendkeys(self.type, text)
        time.sleep(3)
        self.hrm_btn_click(self.hints)
        time.sleep(3)
        self.hrm_btn_click(self.search)
        time.sleep(3)
        self.hrm_btn_click(self.reset)
        time.sleep(3)
        self.scroll(self.addddd)
        time.sleep(5)
        # self.hrm_btn_click(self.checkbox)
        # time.sleep(3)
        # self.hrm_btn_click(self.delete)
        # self.hrm_btn_click(self.dele1)
        # self.hrm_btn_click(self.checkbox1)
        # self.hrm_btn_click(self.dele2)
        # self.hrm_btn_click(self.no_cancel)

    def delete_tracker(self):
        self.hrm_btn_click(self.trash)
        time.sleep(3)
        self.hrm_btn_click(self.yes_delete)
        time.sleep(3)
        self.hrm_btn_click(self.trash1)
        time.sleep(3)
        self.hrm_btn_click(self.no_delete2)
        time.sleep(3)
        self.hrm_btn_click(self.trash2)
        time.sleep(3)
        self.hrm_btn_click(self.close)
        time.sleep(3)

    def edit_tracker(self, text, emp, text1):
        self.hrm_btn_click(self.pencil)
        time.sleep(3)
        self.hrm_sendkeys(self.tracker_name, text)
        time.sleep(3)
        action=ActionChains(self.driver)
        self.hrm_btn_click(self.emp_name)
        action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
        self.hrm_sendkeys(self.emp_name, emp)
        time.sleep(5)
        self.hrm_btn_click(self.name)
        time.sleep(3)
        self.hrm_sendkeys(self.reviewer, text1)
        time.sleep(3)
        self.hrm_btn_click(self.name1)
        time.sleep(3)
        self.hrm_btn_click(self.save)
        time.sleep(3)


        self.scroll(self.addd)
        time.sleep(3)
        self.hrm_btn_click(self.pen)
        time.sleep(3)
        self.hrm_btn_click(self.canc)
        time.sleep(3)

    def add_tracker(self, txt, txt1, txt2):
        self.hrm_btn_click(self.add)
        time.sleep(3)
        self.hrm_sendkeys(self.tracker_name1, txt)
        time.sleep(3)
        self.hrm_sendkeys(self.emp_name1, txt1)
        time.sleep(3)
        self.hrm_btn_click(self.names)
        time.sleep(3)
        self.hrm_sendkeys(self.reviewers, txt2)
        time.sleep(3)
        self.hrm_btn_click(self.name12)
        time.sleep(3)

        self.hrm_btn_click(self.saves)
        time.sleep(3)
        self.hrm_btn_click(self.add1)
        time.sleep(3)
        self.hrm_btn_click(self.cancel)
        time.sleep(3)





