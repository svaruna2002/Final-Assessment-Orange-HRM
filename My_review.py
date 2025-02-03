import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from Basepage import Basepage


class My(Basepage):
    manager = (By.XPATH, "(//span[normalize-space()='Manage Reviews'])[1]")
    my_review = (By.XPATH,"(//a[normalize-space()='My Reviews'])[1]")
    view = (By.XPATH,"(//i[@class='oxd-icon bi-file-text-fill'])[1]")
    first_box = (By.XPATH,"(//input)[2]")
    box = (By.XPATH,"(//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical orangehrm-evaluation-grid-comment'])[1]")
    second_box = (By.XPATH,"(//input)[3]")
    box1 = (By.XPATH,"(//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical orangehrm-evaluation-grid-comment'])[2]")
    third_box = (By.XPATH,"(//input)[4]")
    box2 = (By.XPATH,"(//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical orangehrm-evaluation-grid-comment'])[3]")
    fourth_box = (By.XPATH,"(//input)[5]")
    box3 = (By.XPATH,"(//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical orangehrm-evaluation-grid-comment'])[4]")
    fifth_box = (By.XPATH,"(//input)[6]")
    box4 = (By.XPATH,"(//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical orangehrm-evaluation-grid-comment'])[5]")
    save = (By.XPATH,"//button[normalize-space()='Save']")
    a = (By.XPATH,"(//p[@class='oxd-text oxd-text--p orangehrm-evaluation-grid-general-label'])[1]")
    cancel = (By.XPATH,"(//button[normalize-space()='Cancel'])[1]")

    def __init__(self, driver):
        super().__init__(driver)

    def performance_myreview(self):
        self.hrm_btn_click(self.manager)
        self.hrm_btn_click(self.my_review)
        self.hrm_btn_click(self.view)

    def performance_comments(self, txt, txt1, txt2, txt3, txt4, txt5, txt6, txt7, txt8, txt9):
        self.hrm_sendkeys(self.first_box, txt)
        time.sleep(5)
        self.hrm_sendkeys(self.box, txt1)
        time.sleep(5)
        self.hrm_sendkeys(self.second_box, txt2)
        time.sleep(5)
        self.hrm_sendkeys(self.box1, txt3)
        time.sleep(5)
        self.hrm_sendkeys(self.third_box, txt4)
        time.sleep(5)
        self.hrm_sendkeys(self.box2, txt5)
        time.sleep(5)
        self.hrm_sendkeys(self.fourth_box, txt6)
        time.sleep(5)
        self.hrm_sendkeys(self.box3, txt7)
        time.sleep(5)
        self.hrm_sendkeys(self.fifth_box, txt8)
        time.sleep(5)
        self.hrm_sendkeys(self.box4,txt9)
        time.sleep(5)
        self.hrm_btn_click(self.save)
        time.sleep(5)
        self.scroll(self.a)
        time.sleep(5)
        self.hrm_btn_click(self.cancel)
        time.sleep(5)













