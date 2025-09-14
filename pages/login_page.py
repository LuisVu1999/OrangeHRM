from pages.base_page import BasePage
from pages.locators.login import LoginLocator

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def login(self, username: str, password: str):
        self.fill(LoginLocator.USERNAME_INPUT, username)
        self.fill(LoginLocator.PASSWORD_INPUT, password)
        self.click(LoginLocator.SUBMIT_BUTTON)
        self.is_visible(LoginLocator.PAGE_TITLE)

    def forgot_password(self, username: str, reset_successfully_text: str):
        #1. Click on forgot password
        self.click(LoginLocator.FORGOT_PASSWORD)
        self.fill(LoginLocator.USERNAME_INPUT, username)
        self.click(LoginLocator.SUBMIT_BUTTON)
        self.assert_text_contain(LoginLocator.SUCCESSFULLY_RESET, reset_successfully_text)

    def logout(self, signin_text: str):
        self.click(LoginLocator.AVATAR)
        self.click(LoginLocator.LOGOUT_BUTTON)
        self.assert_text_contain(LoginLocator.SIGNIN_TEXT, signin_text, "Verify Sign In Page")

    def login_with_wrong_pass(self, username: str, password: str, expected_result:str):
        self.fill(LoginLocator.USERNAME_INPUT, username)
        self.fill(LoginLocator.PASSWORD_INPUT, password)
        self.click(LoginLocator.SUBMIT_BUTTON)
        self.assert_text_contain(LoginLocator.INVALID_CREDENTIAL, expected_result)

    def login_empty_credentials(self, expected_result:str):
        self.click(LoginLocator.SUBMIT_BUTTON)
        self.assert_text_contain(LoginLocator.ERROR_USER, expected_result)
        self.assert_text_contain(LoginLocator.ERROR_PASS, expected_result)