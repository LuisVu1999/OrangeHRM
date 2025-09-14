from pages.base_page import BasePage
from pages.locators.admin import AdminLocator

class AdminPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def navigate_to_admin(self):
        self.click(AdminLocator.NAVIGATE_TO_ADMIN)
    
    def create_user(self,page_title: str, user_name: str, password: str, employee_name: str, expected_message: str):
        self.click(AdminLocator.ADD_BUTTON)
        self.assert_text_contain(AdminLocator.PAGE_TITLE, page_title)
        self.click(AdminLocator.ROLE_DROPDOWN)
        self.click(AdminLocator.ESS_ROLE)
        self.click(AdminLocator.STATUS_DROPDOWN)
        self.click(AdminLocator.ENABLE_STATUS)
        self.fill(AdminLocator.USER_NAME, user_name)
        self.fill(AdminLocator.PASSWORD, password)
        self.fill(AdminLocator.CONFIRM_PASSWORD, password)
        self.fill(AdminLocator.EMPLOYEE_NAME, employee_name)
        self.wait_thread_sleep(3)
        self.click(AdminLocator.SELECT_EMPLOYEE)
        self.click(AdminLocator.SAVE_BUTTON)
        self.assert_text_contain(AdminLocator.NOTIFY_MESSAGE, expected_message)

    def view_user(self, user_name: str, role_expected: str, expected_employee_name: str, expected_status: str):
        text = self.page.locator(AdminLocator.VERIFY_USERNAME).inner_text()
        # print(f"actual: {text}")
        # print(f"expected: Title_ggg123")
        print("Expected repr:", repr(text))
        print("Actual repr:", repr("Title_qqq")) 
        # self.wait_thread_sleep(3)
        self.assert_text(AdminLocator.VERIFY_USERNAME, user_name)
        self.assert_text(AdminLocator.VERIFY_ROLE, role_expected)
        self.assert_text(AdminLocator.VERIFY_EMPLOYEE_NAME, expected_employee_name)
        self.assert_text(AdminLocator.VERIFY_STATUS, expected_status)
        self.assert_visible(AdminLocator.VERIFY_ACTION_EDIT)
        self.assert_visible(AdminLocator.VERIFY_ACTION_DELETE)

    def search_user(self, user_name: str):
        self.wait_for_load_page()
        self.fill(AdminLocator.SEARCH_BOX, user_name)
        self.click(AdminLocator.SEARCH_BUTTON)
        self.wait_for_load_page()
        
    def delete_user(self,expected_message: str):
        self.click(AdminLocator.VERIFY_ACTION_DELETE)
        self.click(AdminLocator.CONFIRM_DELETE)
        self.assert_text_contain(AdminLocator.NOTIFY_MESSAGE, expected_message)

    def modify_role(self, expected_title: str, expected_message: str):
        self.click(AdminLocator.VERIFY_ACTION_EDIT)
        self.assert_text_contain(AdminLocator.EDIT_TITLE, expected_title)
        self.click(AdminLocator.ROLE_DROPDOWN)
        self.click(AdminLocator.ADMIN_ROLE)
        self.click(AdminLocator.SAVE_BUTTON)
        self.assert_text_contain(AdminLocator.NOTIFY_MESSAGE, expected_message)

    def create_invalid_user(self, user_name: str, expected_message: str):
        self.click(AdminLocator.ADD_BUTTON)
        self.fill(AdminLocator.USER_NAME, user_name)
        self.assert_text(AdminLocator.INVALID_USERNAME, expected_message)