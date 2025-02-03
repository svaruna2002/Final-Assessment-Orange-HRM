import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="firefox"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "IE":
        driver = webdriver.Edge()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    time.sleep(10)
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.CSS_SELECTOR, ".oxd-input.oxd-input--active").send_keys("admin123")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(5)
    request.cls.driver = driver
    yield
    dropdown_logout = driver.find_element(By.CSS_SELECTOR, ".oxd-userdropdown-name").click()
    time.sleep(3)
    Logout = driver.find_element(By.LINK_TEXT, "Logout").click()
    time.sleep(3)

    driver.quit()