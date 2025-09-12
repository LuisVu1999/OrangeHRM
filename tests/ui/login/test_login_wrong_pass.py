from pages.login_page import LoginPage
from config import Credentials

def test_login_wrong_pass(page):
    login_page = LoginPage(page)
    login_page.login_with_wrong_pass(Credentials.ADMIN_USER, "tttt", "Invalid credentials")