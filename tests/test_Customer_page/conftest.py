import pytest
from playwright.sync_api import Page
from page.customer_page import CustomerPage
from page.login_page import LoginPage

@pytest.fixture
def customer_page(page: Page) -> CustomerPage:
    # Login first
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login("admin@gmail.com", "123456aA@")
    
    # Create customer page
    customer_page = CustomerPage(page)
    customer_page.navigate_to_client()
    return customer_page 