from pages.login_page import LoginPage
from pages.pim_page import PimPage
from pages.leave_page import LeavePage
from config import Credentials
from helpers.test_data import TestData

def test_reject_leave(page):
    login_page = LoginPage(page)
    pim_page = PimPage(page)
    leave_page = LeavePage(page)

    #1. Khoi tao bien
    #1.1.Prepare Data
    first_name_prepare = TestData.random_first_name()
    last_name_prepare = TestData.random_last_name()
    middle_name_prepare = TestData.random_first_name()
    first_middle_last_name_prepare = f"{first_name_prepare} {last_name_prepare}"
    employee_id_prepare = f"197{TestData.random_int()}"
    user_name_prepare = TestData.random_user_name()

    #1.2.Create Emp
    password = TestData.random_password()
    first_name_create = TestData.random_first_name()
    last_name_create = TestData.random_last_name()
    middle_name_create = TestData.random_first_name()
    first_middle_name_create = f"{first_name_create} {middle_name_create}"
    employee_id_create = f"198{TestData.random_int()}"
    user_name_create = TestData.random_user_name()

    #1.3.Modify Emp
    first_name_edited = TestData.random_first_name()
    last_name_edited = TestData.random_last_name()
    middle_name_edited = TestData.random_first_name()
    full_name = f"{first_name_edited} {middle_name_edited} {last_name_edited}"
    employee_id_edited = f"199{TestData.random_int()}"

    #1.4.Add entitlement
    duration = "80"
    add_entitlement_title = "Add Leave Entitlement"
    #1.5.Apply leave
    apply_leave_title = "Apply Leave"
    date_time = "2025-18-11"

    #2. Create Emp
    #2.1.Create Emp
    login_page.login(Credentials.ADMIN_USER, Credentials.ADMIN_PASSWORD)
    pim_page.naviage_to_pim()
    pim_page.create_employee("Add Employee", first_name_prepare, last_name_prepare, middle_name_prepare,
                             employee_id_prepare ,user_name_prepare ,password, password, "Successfully Saved")
    pim_page.naviage_to_pim()
    pim_page.create_employee("Add Employee", first_name_create, last_name_create, middle_name_create,
                             employee_id_create, user_name_create, password, password, "Successfully Saved")
    #2.2.Edit Emp
    pim_page.search_employee(first_middle_name_create)
    pim_page.edit_employee(first_name_edited, last_name_edited, middle_name_edited, employee_id_edited, first_middle_last_name_prepare, "Successfully Updated")

    #2.3.Add Entitlement
    leave_page.navigate_to_leave()
    leave_page.add_entitlement(add_entitlement_title, full_name, duration, "Successfully Saved")
    #Logout from Admin
    login_page.logout("Login")

    #3. Login by End user and apply leave
    login_page.login(user_name_create, password)
    leave_page.navigate_to_leave()
    leave_page.apply_leave(apply_leave_title, date_time, duration, "Successfully Saved")
    login_page.logout("Login")
    
    #4. Login by Admin and reject request
    login_page.login(user_name_prepare, password)
    leave_page.navigate_to_leave()
    leave_page.reject_leave(full_name)