from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from pages.pim_page import PimPage
from config import Credentials
from helpers.test_data import TestData

def test_view_user(page):
    login_page = LoginPage(page)
    pim_page = PimPage(page)
    admin_page = AdminPage(page)

    # user_name= f"Title_{TestData.random_user_name()}"
    # employee_name = "Radha Gupta"

    # login_page.login(Credentials.ADMIN_USER, Credentials.ADMIN_PASSWORD)
    # #Create User
    # admin_page.navigate_to_admin()
    # admin_page.create_user("Add User", user_name, TestData.random_password(), employee_name, "Successfully Saved")
    # #Edit Role
    # admin_page.search_user(user_name)
    # admin_page.modify_role("Edit User", "Successfully Updated")
    # #Delete User
    # admin_page.search_user(user_name)
    # admin_page.delete_user("Successfully Deleted")


    #1. Khai bao bien
    #1.1.Create Emp
    password = TestData.random_password()
    first_name = TestData.random_first_name()
    last_name = TestData.random_last_name()
    middle_name = TestData.random_first_name()
    full_emp_name = f"{first_name} {middle_name} {last_name}"
    first_last_emp_name = f"{first_name} {last_name}"

    #1.2.Create User Role
    user_name_role = f"Title_{TestData.random_user_name()}"

    #2. Create Emp
    login_page.login(Credentials.ADMIN_USER, Credentials.ADMIN_PASSWORD)
    pim_page.naviage_to_pim()
    pim_page.create_employee("Add Employee", first_name, last_name, middle_name,
                             f"196{TestData.random_int()}",TestData.random_user_name(),password, password, "Successfully Saved")

    #3. Create Role
    admin_page.navigate_to_admin()
    admin_page.create_user("Add User", user_name_role, TestData.random_password(), full_emp_name, "Successfully Saved")

    #4. Edit Role
    admin_page.search_user(user_name_role)
    admin_page.modify_role("Edit User", "Successfully Updated")

    #5. Delete Role
    admin_page.search_user(user_name_role)
    admin_page.delete_user("Successfully Deleted")