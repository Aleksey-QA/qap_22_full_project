import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class BaseElement:

    def __init__(self, driver, selector=None, type_of_locator=By.CSS_SELECTOR, timeout=10):
        self.driver: WebDriver = driver
        self.type_of_locator = type_of_locator
        self.selector: str = selector
        if self.selector.startswith('//'):
            self.type_of_locator = By.XPATH
        else:
            self.type_of_locator = By.CSS_SELECTOR

        self.locator = (self.type_of_locator, self.selector)

        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Wait for: {locator}")
    def wait_visible(self):
        el = self.wait.until(EC.visibility_of_element_located(self.locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
        return el

    @allure.step("Click on: {locator} with force={is_force}")
    def click(self, is_force=False):
        el = self.wait.until(EC.element_to_be_clickable(self.locator))
        if is_force:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
            self.driver.execute_script("arguments[0].click();", el)

        else:
            el.click()

    def send_keys(self, value):
        el = self.wait_visible(self.locator)
        el.send_keys(value)

    def select_item_by_value(self, value):
        el = self.wait_visible(self.locator)
        select = Select(el)
        select.select_by_value(value)

    def select_item_by_visible_text(self, visible_text):
        el = self.wait_visible(self.locator)
        select = Select(el)
        select.select_by_visible_text(visible_text)

    def assert_element_visible(self):
        el = self.wait_visible(self.locator)
        assert el.is_displayed(), f"Element '{self.locator[-1]}' does not found on the page"

    def assert_text_in_element(self, text):
        el = self.wait_visible(self.locator)
        assert el.text == text, f"Element '{self.locator[-1]}' does not have text: {text}"

    def assert_text_contain_in_element(self, text):
        el = self.wait_visible(self.locator)
        assert text in el.text, f"Element '{self.locator[-1]}' does not contain text: {text}"
