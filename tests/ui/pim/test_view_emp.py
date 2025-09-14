from pages.login_page import LoginPage
from pages.pim_page import PimPage
from config import Credentials
from helpers.test_data import TestData

def test_view_empy(page):
    login_page = LoginPage(page)
    pim_page = PimPage(page)

    password = TestData.random_password()
    first_name = TestData.random_first_name()
    last_name = TestData.random_last_name()
    middle_name = TestData.random_first_name()
    first_middle_name = f"{first_name} {middle_name}"
    employee_id = f"187{TestData.random_int()}"
    user_name = TestData.random_user_name()

    #Create Employee
    login_page.login(Credentials.ADMIN_USER, Credentials.ADMIN_PASSWORD)
    pim_page.naviage_to_pim()
    pim_page.create_employee("Add Employee", first_name, last_name, middle_name,
                             employee_id,user_name,password, password, "Successfully Saved")
    
    #View employee
    pim_page.search_employee(first_middle_name)
    pim_page.view_employee(employee_id, first_middle_name, last_name)