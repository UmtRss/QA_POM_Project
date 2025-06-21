# tests/test_login_valid.py
from pages.login_page import LoginPage

def test_valid_login(browser):
    page = LoginPage(browser)
    page.login("student", "Password123")
    assert "Logged In Successfully" in page.get_title()
