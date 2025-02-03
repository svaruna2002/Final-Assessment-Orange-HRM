import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="Firefox")


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "Chrome":
        driver = webdriver.Chrome()
    elif browser_name == "Edge":
        driver = webdriver.Edge()
    elif browser_name == "Firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser!")

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(10)  # Replace time.sleep with implicit wait for stability
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    request.cls.driver = driver
    yield
    # Teardown logic
    driver.find_element(By.CSS_SELECTOR, ".oxd-userdropdown-name").click()
    driver.find_element(By.LINK_TEXT, "Logout").click()
    driver.quit()
