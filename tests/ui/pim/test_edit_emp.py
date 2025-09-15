from pages.login_page import LoginPage
from pages.pim_page import PimPage
from config import Credentials
from helpers.test_data import TestData

def test_edit_empy(page):
    login_page = LoginPage(page)
    pim_page = PimPage(page)

    #Prepare Data
    first_name_prepare = TestData.random_first_name()
    last_name_prepare = TestData.random_last_name()
    middle_name_prepare = TestData.random_first_name()
    first_middle_last_name_prepare = f"{first_name_prepare} {last_name_prepare}"
    employee_id_prepare = f"194{TestData.random_int()}"
    user_name_prepare = f"title101_{TestData.random_user_name()}"

    #Create Emp
    password = TestData.random_password()
    first_name_create = TestData.random_first_name()
    last_name_create = TestData.random_last_name()
    middle_name_create = TestData.random_first_name()
    first_middle_name_create = f"{first_name_create} {middle_name_create}"
    employee_id_create = f"193{TestData.random_int()}"
    user_name_create = f"title102_{TestData.random_user_name()}"

    #Modify Emp
    first_name_edited = TestData.random_first_name()
    last_name_edited = TestData.random_last_name()
    middle_name_edited = TestData.random_first_name()
    first_middle_name_edited = f"{first_name_edited} {middle_name_edited}"
    employee_id_edited = f"192{TestData.random_int()}"
    job_title = "QA Engineer"
    employee_status = "Full-Time Contract"
    sub_unit = "Engineering"

    
    login_page.login(Credentials.ADMIN_USER, Credentials.ADMIN_PASSWORD)
    pim_page.naviage_to_pim()

    #Prepare data:
    pim_page.create_employee("Add Employee", first_name_prepare, last_name_prepare, middle_name_prepare,
                             employee_id_prepare ,user_name_prepare ,password, password, "Successfully Saved")
    pim_page.naviage_to_pim()

    #Create Employee
    pim_page.create_employee("Add Employee", first_name_create, last_name_create, middle_name_create,
                             employee_id_create, user_name_create, password, password, "Successfully Saved")
    
    #Edit Emp
    pim_page.search_employee(first_middle_name_create)
    pim_page.edit_employee(first_name_edited, last_name_edited, middle_name_edited, employee_id_edited, first_middle_last_name_prepare, "Successfully Updated")

    #View Employee
    pim_page.search_employee(first_middle_name_edited)
    pim_page.view_employee_after_edited(employee_id_edited, first_middle_name_edited, last_name_edited, job_title, employee_status, sub_unit, first_middle_last_name_prepare)