from pages.login_page import LoginPage
from config import Credentials

def test_forgot_password(page):
    login_page = LoginPage(page)
    login_page.forgot_password(Credentials.ADMIN_USER, "Reset Password link sent successfully")