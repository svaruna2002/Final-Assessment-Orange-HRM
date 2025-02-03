from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
driver.maximize_window()

#login
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
time.sleep(3)
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
time.sleep(5)

#navigating to Performance Page
driver.find_element(By.LINK_TEXT, "Performance").click()
time.sleep(5)

#navigating to employee tracker
driver.find_element(By.XPATH, "//a[normalize-space()='Employee Trackers']").click()
time.sleep(5)

#employee name
driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']").send_keys("peter")
time.sleep(5)

driver.find_element(By.XPATH, "//span[normalize-space()='Peter Mac Anderson']").click()
time.sleep(5)

#include
driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']").click()
time.sleep(5)

driver.find_element(By.XPATH, "//span[normalize-space()='Past Employees Only']").click()
time.sleep(5)

#search
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(3)

#reset
driver.find_element(By.CSS_SELECTOR, "button[type='reset']").click()
time.sleep(3)

#view
driver.find_element(By.CSS_SELECTOR, "button[name='view']").click()
time.sleep(3)

#add log
driver.find_element(By.XPATH, "//button[normalize-space()='Add Log']").click()
time.sleep(3)

#entering a log
driver.find_element(By.XPATH, "//input[@placeholder='Type here']").send_keys("Agility")
time.sleep(5)

#positive review
driver.find_element(By.XPATH, "//button[normalize-space()='Positive']").click()
time.sleep(5)

#comment
driver.find_element(By.XPATH, "//textarea[@placeholder='Type here']").send_keys("Finish the work")
time.sleep(5)

#save
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
time.sleep(3)

#cancel
# driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()
# time.sleep(5)


#PART 2 MY TRACKER PAGE
#navigating to my tracker page
driver.find_element(By.XPATH, "//a[normalize-space()='My Trackers']").click()
time.sleep(3)

#view
driver.find_element(By.CSS_SELECTOR, "button[name='view']").click()
time.sleep(3)

#add button
driver.find_element(By.XPATH, "//button[normalize-space()='Add Log']").click()
time.sleep(3)

#log
driver.find_element(By.XPATH, "//input[@placeholder='Type here']").send_keys("Time Management")
time.sleep(3)

#negative
driver.find_element(By.XPATH, "//button[normalize-space()='Negative']").click()
time.sleep(3)

#comment
driver.find_element(By.XPATH, "//textarea[@placeholder='Type here']").send_keys("Try to improve")
time.sleep(5)

#save
driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
time.sleep(3)

#cancel
# driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()
# time.sleep(3)
