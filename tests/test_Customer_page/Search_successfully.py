import pytest
from playwright.sync_api import Page
from page.customer_page import CustomerPage

def test_search_customer(customer_page: CustomerPage):
    # TC_02: Search successfully
    customer_page.search_bar.fill("User")
    assert customer_page.page.locator("text=user").is_visible() 