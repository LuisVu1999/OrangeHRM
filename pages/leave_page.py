from pages.base_page import BasePage
from pages.locators.leave import LeaveLocator

class LeavePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def navigate_to_leave(self):
        self.click(LeaveLocator.NAGIVATE_TO_LEAVE)
        self.wait_for_load_page()

    def add_entitlement(self, add_entitlement_title: str, employee_name: str, duration: str, successfully_message: str):
        self.click(LeaveLocator.ENTITLEMENT_DROPDOWN)
        self.click(LeaveLocator.ADD_ENTITLEMENT)
        self.wait_thread_sleep(2)
        self.assert_text(LeaveLocator.ADD_ENTITLEMENT_TITLE, add_entitlement_title, "verify entitlment title")
        self.assert_is_selected(LeaveLocator.INVIDUAL_EMPLOYEE, "verify invidual checked")
        self.fill(LeaveLocator.EMPLOYEE_NAME, employee_name)
        self.wait_thread_sleep(2)
        self.click(LeaveLocator.SELECT_EMPLOYEE)
        self.click(LeaveLocator.LEAVE_TYPE_DROPDOWN)
        self.click(LeaveLocator.SELECT_VACATION)
        self.fill(LeaveLocator.ENTITLEMENT, duration)
        self.click(LeaveLocator.SAVE_BUTTON)
        self.click(LeaveLocator.CONFIRM_BUTTON)
        self.assert_text_contain(LeaveLocator.NOTIFY_MESSAGE, successfully_message)

    def apply_leave(self, apply_leave_title: str, date_time: str, leave_balance: str, successfully_message: str):
        self.click(LeaveLocator.CLICK_APPLY)
        self.wait_thread_sleep(2)
        self.assert_text(LeaveLocator.APPLY_LEAVE_TITLE, apply_leave_title, "verify apply title")
        self.click(LeaveLocator.LEAVE_TYPE_DROPDOWN)
        self.click(LeaveLocator.SELECT_VACATION_APPLY)
        self.fill(LeaveLocator.SELECT_FROM_DATE, date_time)
        self.wait_thread_sleep(2)
        self.click(LeaveLocator.SELECT_TO_DATE)
        self.click(LeaveLocator.DURATION_DROPDOWN)
        self.click(LeaveLocator.SELECT_HALF_MORNING)
        self.assert_text_contain(LeaveLocator.LEAVE_BALANCE, leave_balance, "verify leave balance")
        self.click(LeaveLocator.SAVE_BUTTON)
        self.assert_text_contain(LeaveLocator.NOTIFY_MESSAGE, successfully_message)

    def reject_leave(self, employee_name: str):
        self.fill(LeaveLocator.EMPLOYEE_NAME, employee_name)
        self.wait_thread_sleep(3)
        self.click(LeaveLocator.SELECT_EMPLOYEE)
        self.click(LeaveLocator.SAVE_BUTTON)
        self.click(LeaveLocator.REJECT_BUTTON)

    def approve_leave(self, employee_name: str, date_approve: str, leave_type: str, balance: str, 
                     number_day: str, status: str):
        self.fill(LeaveLocator.EMPLOYEE_NAME, employee_name)
        self.wait_thread_sleep(3)
        self.click(LeaveLocator.SELECT_EMPLOYEE)
        self.click(LeaveLocator.SAVE_BUTTON)
        self.wait_thread_sleep(2)
        self.assert_text(LeaveLocator.DATE_APPROVE, date_approve, "verify date approve")
        self.assert_text(LeaveLocator.EMPLOYEE_APPROVE, employee_name, "verify employee name")
        self.assert_text(LeaveLocator.LEAVE_TYPE_APPROVE, leave_type, "verify leave type")
        self.assert_text(LeaveLocator.LEAVE_BALANCE_APPROVE, balance, "verify balance")
        self.assert_text(LeaveLocator.NUMBER_DAYS_APPROVE, number_day, "verify number day")
        self.assert_text(LeaveLocator.STATUS_APPROVE, status, "verify status")
        self.click(LeaveLocator.APPROVE_BUTTON)

