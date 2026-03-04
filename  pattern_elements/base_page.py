import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config import BaseConfig


class BasePage:

    def __init__(self, driver, url=None, timeout=BaseConfig.WEB_DRIVER_WAIT, title='Task Management Board'):
        self.driver: WebDriver = driver
        self.url = url
        self.title = title

        self.wait = WebDriverWait(driver, timeout)

    def open(self, with_path=None):
        with allure.step(f"Open page: {self.url}"):
            url = f"{BaseConfig.ROOT_PATH}{self.url}{with_path}" if with_path else f"{BaseConfig.ROOT_PATH}{self.url}"
            self.driver.get(url)

    def wait_page_opened(self):
        with  allure.step(f"Wait for page: {self.url}"):
            self.wait.until(EC.url_contains(self.url))

    def assert_that_page_opened(self):
        self.wait_page_opened()

        assert self.url in self.driver.current_url, f"Expected: {self.url}, but {self.driver.current_url}"
        assert self.title == self.driver.title
