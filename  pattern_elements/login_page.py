import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from base_element import BaseElement
from base_page import BasePage
from test_data.users import User


class LoginPage(BasePage):
    def __init__(self, driver):
        self.url = '/login'

        self.LOGIN_INPUT: BaseElement = BaseElement(self.driver, 'id-input-login-email-input', By.ID)
        self.PASSWORD_INPUT: BaseElement = BaseElement(self.driver, '[id="id-input-login-password-input"]')
        self.SUBMIT: BaseElement = BaseElement(self.driver, '//*[@data-qa="login-submit-button"]', By.XPATH)

        super().__init__(driver, self.url)
        self.driver: WebDriver = driver

    @allure.step("Login with email {user}")
    def login(self, user: User):
        self.LOGIN_INPUT.send_keys(user.email)
        self.PASSWORD_INPUT.send_keys(user.password)

        self.SUBMIT.click()
