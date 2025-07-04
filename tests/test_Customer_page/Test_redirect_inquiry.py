import pytest
from playwright.sync_api import Page
from page.customer_page import CustomerPage

def test_redirect_inquiry(customer_page: CustomerPage):

    # TC_05: Test redirect inquiry
    customer_page.navigate_to_client()
    customer_page.page.locator('a:has-text("rye")').click()
    first_content = customer_page.get_conversation_content()
    customer_page.click_inquiry_card(1)
    second_content = customer_page.get_conversation_content()
    assert first_content != second_content 