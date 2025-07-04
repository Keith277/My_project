import pytest
from playwright.sync_api import Page
from page.customer_page import CustomerPage

def test_add_source_success(customer_page: CustomerPage):
    # TC_07: Test Add Source successfully
    customer_page.page.goto("https://cx-call-center-dev.talena.ai/knowledge")
    customer_page.add_source("Test4", "C:\\Users\\keith.nguyen\\Downloads\\Anastasiia Fomkina.pdf")
    customer_page.page.wait_for_timeout(1000)
    assert customer_page.page.locator("text=Test4").is_visible() 