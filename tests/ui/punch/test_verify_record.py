from pages.punch_page import PunchPage
from pages.login_page import LoginPage
from config import Credentials

def test_verify_record(page):
    login_page = LoginPage(page)
    punch_page = PunchPage(page)

    hour = "10"
    minute = "30"
    date_punch = "2025-18-11"
    punch_in_time = f"{date_punch} - {hour}:{minute} AM (GMT +07:00)"
    time_out = "04:30 PM"
    punch_in_record = "2025-18-11 10:30 AM "
    punch_out_record = "2025-18-11 04:30 PM "
    total_hour = "Total Duration (Hours): 6.00"
    duration = "6.00"

    #Navigate to Time
    login_page.login(Credentials.ADMIN_USER, Credentials.ADMIN_PASSWORD)
    punch_page.navigate_to_time()
    #Punch in/out
    punch_page.punch_in_out("Punch In", hour, minute, "Successfully Saved", "Punch Out", punch_in_time, date_punch, time_out)
    #Check Record
    punch_page.verify_record(date_punch, total_hour, punch_in_record, punch_out_record, duration)
    #Delete Record
    punch_page.delete_record(date_punch)