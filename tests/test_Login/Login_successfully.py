import pytest
from playwright.sync_api import Page
from page.login_page import LoginPage

def test_login_successful(page: Page):
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login("admin@gmail.com", "123456aA@")
    assert login_page.is_on_client_page() 