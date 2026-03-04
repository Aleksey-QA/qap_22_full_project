from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Assertions:

    def __init__(self, driver, locator, timeout):
        self.driver: WebDriver = driver
        self.locator = locator
        self.wait = WebDriverWait(driver, timeout)

    def assert_element_visible(self):
        assert self.locator.is_displayed(), f"Element '{self.locator[-1]}' does not found on the page"

    def assert_text_in_element(self, text):
        assert self.locator.text == text, f"Element '{self.locator[-1]}' does not have text: {text}"

    def assert_text_contain_in_element(self, text):
        assert text in self.locator.text, f"Element '{self.locator[-1]}' does not contain text: {text}"
