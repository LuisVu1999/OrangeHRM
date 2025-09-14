from pages.base_page import BasePage
from pages.locators.punch import PunchLocator

class PunchPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def navigate_to_time(self):
        self.click(PunchLocator.NAVIGATE_TO_TIME)

    def punch_in_out(self, punch_in_title: str, hour: str, minute: str, punch_successfully: str,
                punch_out_title: str, punch_in_time: str, date: str, time: str):
        self.wait_for_load_page()
        self.click(PunchLocator.ATTENDENCE_DROPDOWN)
        self.click(PunchLocator.CLICK_PUNCH)
        self.wait_for_load_page()
        self.wait_thread_sleep(4)
        # self.assert_text(PunchLocator.PUNCH_IN_TITLE, punch_in_title, "verify punch in title")
        #Punch in
        self.click(PunchLocator.CLICK_DATE)
        self.click(PunchLocator.CLICK_YEAR)
        self.click(PunchLocator.SELECT_YEAR)
        self.click(PunchLocator.CLICK_MONTH)
        self.click(PunchLocator.SELECT_MONTH)
        self.click(PunchLocator.SELECT_DATE)

        self.click(PunchLocator.CLICK_TIME)
        self.fill(PunchLocator.HOUR, hour)
        self.fill(PunchLocator.MINUTE, minute)
        self.click(PunchLocator.SELECT_AM)
        self.click(PunchLocator.SUBMIT_BUTTON)
        self.assert_text_contain(PunchLocator.NOTIFY_MESSAGE, punch_successfully, "verify punch successfully")

        #Punch out
        self.wait_for_load_page()
        self.wait_thread_sleep(4)
        self.assert_text(PunchLocator.PUNCH_OUT_TITLE, punch_out_title, "verify punch out title")
        self.assert_text(PunchLocator.PUNCH_IN_TIME, punch_in_time, "verify punch in time")
        self.fill(PunchLocator.CLICK_DATE_OUT, date)
        self.fill(PunchLocator.CLICK_TIME_OUT, time)
        self.click(PunchLocator.SUBMIT_BUTTON)
        self.assert_text_contain(PunchLocator.NOTIFY_MESSAGE, punch_successfully, "verify punch successfully")

    def delete_record(self, date: str):
        self.wait_for_load_page()
        self.click(PunchLocator.ATTENDENCE_DROPDOWN)
        self.click(PunchLocator.CLICK_RECORD)
        self.wait_for_load_page()
        self.fill(PunchLocator.CLICK_DATE, date)
        self.click(PunchLocator.SUBMIT_BUTTON)
        self.click(PunchLocator.DELETE_BUTTON)
        self.click(PunchLocator.CONFIRM_DELETE)
        self.wait_for_load_page()

    def verify_record(self, date: str, total_hour: str, punch_in_time: str, punch_out_time: str, duration: str):
        self.wait_for_load_page()
        self.click(PunchLocator.ATTENDENCE_DROPDOWN)
        self.click(PunchLocator.CLICK_RECORD)
        self.wait_for_load_page()
        self.fill(PunchLocator.CLICK_DATE, date)
        self.click(PunchLocator.SUBMIT_BUTTON)
        self.wait_for_load_page()
        self.wait_thread_sleep(2)
        self.assert_text(PunchLocator.VERIFY_TOTAL_HOUR, total_hour, "verify total hour")
        self.assert_text_contain(PunchLocator.VERIFY_PUNCH_IN, punch_in_time, "verify punch in time")
        self.assert_text_contain(PunchLocator.VERIFY_PUNCH_OUT, punch_out_time, "verify punch out time")
        self.assert_text(PunchLocator.VERIFY_DURATION, duration, "verify duration hour")




