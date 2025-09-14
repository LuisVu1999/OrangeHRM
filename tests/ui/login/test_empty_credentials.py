from pages.login_page import LoginPage

def test_empty_credentials(page):
    login_page = LoginPage(page)
    login_page.login_empty_credentials("Required")