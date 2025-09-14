from pages.admin_page import AdminPage
from pages.login_page import LoginPage
from pages.pim_page import PimPage
from config import Credentials
from helpers.test_data import TestData

def test_create_invalid_user(page):
    login_page = LoginPage(page)
    pim_page = PimPage(page)
    admin_page = AdminPage(page)

    # user_name = f"Title_{TestData.random_user_name()}"

    # login_page.login(Credentials.ADMIN_USER, Credentials.ADMIN_PASSWORD)
    # admin_page.navigate_to_admin()
    # admin_page.create_user("Add User", user_name, TestData.random_password(), "Radha Gupta", "Successfully Saved")

    # admin_page.create_invalid_user(user_name, "Already exists")

    password = TestData.random_password()
    first_name = TestData.random_first_name()
    last_name = TestData.random_last_name()
    middle_name = TestData.random_first_name()
    user_name = TestData.random_user_name()

    login_page.login(Credentials.ADMIN_USER, Credentials.ADMIN_PASSWORD)
    #1. Create emp
    pim_page.naviage_to_pim()
    pim_page.create_employee("Add Employee", first_name, last_name, middle_name,
                             f"196{TestData.random_int()}", user_name, password, password, "Successfully Saved")

    #2. Create role
    admin_page.navigate_to_admin()
    admin_page.create_invalid_user(user_name, "Already exists")