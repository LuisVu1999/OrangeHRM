from pages.base_page import BasePage
from pages.locators.dashboard import DashboardLocator

class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def time_work(self, expected_title: str):
        self.assert_text_contain(DashboardLocator.TIME_WORK_TITLE, expected_title, "Check timework")
        self.assert_visible(DashboardLocator.TIME_WIDGET)

    def my_action(self, expected_title: str):
        self.assert_text_contain(DashboardLocator.MY_ACTION_TITLE, expected_title, "Check my action")
        self.assert_visible(DashboardLocator.ACTION_WIDGET)

    def quick_launch(self, expected_title: str):
        self.assert_text_contain(DashboardLocator.QUICK_LAUNCH_TITLE, expected_title, "Check quick launch")
        self.assert_visible(DashboardLocator.QUICK_LAUNCH_WIDGET)

    def lastes_photo(self, expected_title: str):
        self.assert_text_contain(DashboardLocator.LASTEST_PHOTO_TITLE, expected_title, "Check lastest photo")
        self.assert_visible(DashboardLocator.LASTEST_PHOTO_WIDGET)

    def leave(self, expected_title: str):
        self.assert_text_contain(DashboardLocator.LEAVE_TITLE, expected_title, "Check time leave")
        self.assert_visible(DashboardLocator.LEAVE_WIDGET)

    def distribution_sub_unit(self, expected_title: str):
        self.assert_text_contain(DashboardLocator.DISTRIBUTION_SUBUNIT_TITLE, expected_title, "Check employee sub unit")
        self.assert_visible(DashboardLocator.EMPLOYEE_DISTRIBUTION_WIDGET)

    def distribution_location(self, expected_title: str):
        self.assert_text_contain(DashboardLocator.DISTRIBUTION_LOCATION_TITLE, expected_title, "Check employee location")
        self.assert_visible(DashboardLocator.EMPLOYEE_LOCATION_WIDGET)

