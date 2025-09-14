from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config import Credentials

def test_dashboard(page):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    #Login
    login_page.login(Credentials.ADMIN_USER, Credentials.ADMIN_PASSWORD)

    #Check time_work
    dashboard_page.time_work("Time at Work")

    #Check my_action
    dashboard_page.my_action("My Actions")

    #Check quick_launch
    dashboard_page.quick_launch("Quick Launch")

    #Check lastes_photo
    dashboard_page.lastes_photo("Buzz Latest Posts")

    #Check leave
    dashboard_page.leave("Employees on Leave Today")

    #Check distribution_sub_unit
    dashboard_page.distribution_sub_unit("Employee Distribution by Sub Unit")

    #Check distribution_location
    dashboard_page.distribution_location("Employee Distribution by Location")