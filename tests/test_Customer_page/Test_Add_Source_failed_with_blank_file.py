import pytest
from playwright.sync_api import Page
from page.customer_page import CustomerPage

def test_add_source_failed_blank_file(customer_page: CustomerPage):
    # TC_08: Test Add Source failed with blank file
    customer_page.page.goto("https://cx-call-center-dev.talena.ai/knowledge")
    customer_page.add_source("Test3")
    assert customer_page.is_error_message_visible("Required") 