from pages.login_page import LoginPage
from config import Credentials

def test_login(page):
    login_page = LoginPage(page)
    login_page.login(Credentials.ADMIN_USER, Credentials.ADMIN_PASSWORD)
    login_page.logout("Login")