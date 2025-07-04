import pytest
from playwright.sync_api import Page
from page.customer_page import CustomerPage

def test_check_table(customer_page: CustomerPage):
    # TC_01: Checking table
    headers = ["Customer", "Customer ID", "Phone Number", "Inquiry", "Last Inquiry Date"]
    for header in headers:
        assert customer_page.page.locator(f"text={header}").first.is_visible(), f"Header '{header}' is not visible"