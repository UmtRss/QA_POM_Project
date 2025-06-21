from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def find(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))

    def click(self,locator):
        self.find(locator).click()

    def type(self, locator, input_text):
        self.find(locator).clear()
        self.find(locator).send_keys(input_text)

    def get_title(self):
        return self.driver.title

