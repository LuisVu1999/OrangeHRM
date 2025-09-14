from pages.login_page import LoginPage
from pages.punch_page import PunchPage
from config import Credentials

def test_punch(page):
    login_page = LoginPage(page)
    punch_page = PunchPage(page)

    hour = "10"
    minute = "30"
    date_punch = "2025-18-11"
    punch_in_time = f"{date_punch} - {hour}:{minute} AM (GMT +07:00)"
    time_out = "04:30 PM"

    login_page.login(Credentials.ADMIN_USER, Credentials.ADMIN_PASSWORD)
    punch_page.navigate_to_time()

    punch_page.punch_in_out("Punch In", hour, minute, "Successfully Saved", "Punch Out", punch_in_time, date_punch, time_out)
    punch_page.delete_record(date_punch)