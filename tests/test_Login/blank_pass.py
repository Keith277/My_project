import pytest
from playwright.sync_api import Page
from page.login_page import LoginPage

def test_login_blank_password(page: Page):
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login("admin@gmail.com", "")
    assert login_page.is_error_message_visible("Required") 