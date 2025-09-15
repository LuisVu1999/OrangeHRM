from pages.pim_page import PimPage
from pages.login_page import LoginPage
from config import Credentials
from helpers.test_data import TestData

def test_create_emp(page):
    login_page = LoginPage(page)
    pim_page = PimPage(page)
    password = TestData.random_password()

    login_page.login(Credentials.ADMIN_USER, Credentials.ADMIN_PASSWORD)
    pim_page.naviage_to_pim()
    pim_page.create_employee("Add Employee", TestData.random_first_name(), TestData.random_last_name(), TestData.random_first_name(),
                             f"196{TestData.random_int()}",f"title8_{TestData.random_user_name()}",password, password, "Successfully Saved")