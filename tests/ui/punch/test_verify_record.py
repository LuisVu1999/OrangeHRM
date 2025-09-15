from pages.punch_page import PunchPage
from pages.login_page import LoginPage
from pages.pim_page import PimPage
from config import Credentials
from helpers.test_data import TestData

def test_verify_record(page):
    login_page = LoginPage(page)
    punch_page = PunchPage(page)
    pim_page = PimPage(page)

    hour = "10"
    minute = "30"
    date_punch = "2025-18-11"
    punch_in_time = f"{date_punch} - {hour}:{minute} AM"
    time_out = "04:30 PM"
    punch_in_record = "2025-18-11 10:30 AM "
    punch_out_record = "2025-18-11 04:30 PM "
    total_hour = "Total Duration (Hours): 6.00"
    duration = "6.00"
    password = TestData.random_password()
    user_name = f"Ttitle104_{TestData.random_user_name()}"

    #1. Create emp
    login_page.login(Credentials.ADMIN_USER, Credentials.ADMIN_PASSWORD)
    pim_page.naviage_to_pim()
    pim_page.create_employee("Add Employee", TestData.random_first_name(), TestData.random_last_name(), TestData.random_first_name(),
                             f"196{TestData.random_int()}", user_name, password, password, "Successfully Saved")
    login_page.logout("Login")

    #2. Navigate to Time and Punch in/out
    login_page.login(user_name, password)
    punch_page.navigate_to_time()

    #2.1.Punch in/out
    punch_page.punch_in_out("Punch In", hour, minute, "Successfully Saved", "Punch Out", punch_in_time, date_punch, time_out)
    #2.2.Check Record
    punch_page.verify_record(date_punch, total_hour, punch_in_record, punch_out_record, duration)
    #2.3.Delete Record
    punch_page.delete_record(date_punch)