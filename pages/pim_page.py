from pages.base_page import BasePage
from pages.locators.pim import PimLocator

class PimPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def naviage_to_pim(self):
        self.click(PimLocator.NAVIGATE_TO_PIM)

    def create_employee(self, expected_title: str, first_name: str, last_name: str, middle_name: str, 
                        employee_id: str, user_name: str, password: str,
                        confirm_password: str, crated_successfully: str):
        self.wait_for_load_page()
        self.click(PimLocator.ADD_BUTTON)
        self.wait_thread_sleep(2)
        self.assert_text(PimLocator.PAGE_TITLE, expected_title)
        self.upload_file(PimLocator.UPLOAD_BUTTON, "resources/avt.jpg")
        self.fill(PimLocator.FIRST_NAME, first_name)
        self.fill(PimLocator.LAST_NAME, last_name)
        self.fill(PimLocator.MIDDLE_NAME, middle_name)
        self.fill(PimLocator.EMPLOYEE_ID, employee_id)
        self.click(PimLocator.ENABLE_PASSWORD)
        self.fill(PimLocator.USER_NAME, user_name)
        self.fill(PimLocator.PASSWORD, password)
        self.fill(PimLocator.CONFIRM_PASSWORD, confirm_password)
        self.click(PimLocator.SAVE_BUTTON)
        self.assert_text_contain(PimLocator.NOTIFY_MESSAGE, crated_successfully)

    def view_employee(self, employee_id: str, first_middle_name: str, last_name: str):
        self.wait_for_load_page()
        self.assert_text(PimLocator.VERIFY_ID, employee_id)
        self.assert_text(PimLocator.VERIFY_FIRST_MIDDLE_NAME, first_middle_name)
        self.assert_text(PimLocator.VERIFY_LAST_NAME, last_name)
        self.assert_visible(PimLocator.VERIFY_ACTION_EDIT)
        self.assert_visible(PimLocator.VERIFY_ACTION_DELETE)

    def edit_employee(self, first_name: str, last_name:str, middle_name: str, emp_id:str, supervisor_name: str, edit_successfully: str):
        self.wait_for_load_page()
        self.wait_thread_sleep(3)
        self.click(PimLocator.VERIFY_FIRST_MIDDLE_NAME)
        self.wait_for_load_page()
        self.fill(PimLocator.FIRST_NAME, first_name)
        self.fill(PimLocator.LAST_NAME, last_name)
        self.fill(PimLocator.MIDDLE_NAME, middle_name)
        self.fill(PimLocator.EDIT_EMP_ID, emp_id)
        self.click(PimLocator.SAVE_BUTTON_EDITED)
        self.assert_text_contain(PimLocator.NOTIFY_MESSAGE, edit_successfully)

        self.click(PimLocator.CLICK_JOB)
        # self.click(PimLocator.CLICK_JOB_DROPDOWN)
        # self.click(PimLocator.SELECT_TESTER)
        self.click(PimLocator.CLICK_STATUS)
        self.click(PimLocator.SELECT_FULLTIME)
        self.click(PimLocator.CLICK_SUBUNIT)
        self.click(PimLocator.SELECT_ENGINEERING)
        self.click(PimLocator.SAVE_BUTTON_EDITED)
        self.assert_text_contain(PimLocator.NOTIFY_MESSAGE, edit_successfully)

        self.click(PimLocator.CLICK_REPORT_TO)
        self.click(PimLocator.CLICK_ADD_BUTTON)
        self.fill(PimLocator.SUPERVISOR_NAME, supervisor_name)
        self.wait_thread_sleep(3)
        self.click(PimLocator.SELECT_USER)
        self.click(PimLocator.CLICK_METHOD)
        self.click(PimLocator.SELECT_DIRECT)
        self.click(PimLocator.SAVE_BUTTON_EDITED)
        self.assert_text_contain(PimLocator.NOTIFY_MESSAGE, "Successfully Saved")

    def delete_employee(self, deleted_successfully: str):
        self.wait_thread_sleep(3)
        self.click(PimLocator.VERIFY_ACTION_DELETE)
        self.click(PimLocator.CONFIRM_DELETE)
        self.assert_text_contain(PimLocator.NOTIFY_MESSAGE, deleted_successfully)

    def search_employee(self, employee_name: str):
        self.click(PimLocator.CLICK_LIST)
        self.wait_for_load_page()
        self.fill(PimLocator.SEARCH_BOX, employee_name)
        self.wait_thread_sleep(3)
        self.click(PimLocator.SELECT_EMP)
        self.click(PimLocator.SEARCH_BUTTON)
        self.wait_for_load_page()

    def view_employee_after_edited(self, employee_id: str, first_middle_name: str, last_name: str,
                                   job_title: str, employee_status: str, sub_unit: str, supervisor: str):
        self.wait_for_load_page()
        self.assert_text(PimLocator.VERIFY_ID, employee_id)
        self.assert_text(PimLocator.VERIFY_FIRST_MIDDLE_NAME, first_middle_name)
        self.assert_text(PimLocator.VERIFY_LAST_NAME, last_name)
        # self.assert_text(PimLocator.VERIFY_JOB_TITLE, job_title)
        self.assert_text(PimLocator.VERIFY_EMPLOYEE_STATUS, employee_status)
        self.assert_text(PimLocator.VERIFY_SUB_UNIT, sub_unit)
        self.assert_text(PimLocator.VERIFY_SUPPERVISOR, supervisor)
