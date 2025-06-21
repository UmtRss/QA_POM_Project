# conftest.py
import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")  # örnek login sayfası
    driver.maximize_window()
    yield driver
    driver.quit()
