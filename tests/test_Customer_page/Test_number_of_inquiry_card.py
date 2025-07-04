import pytest
from playwright.sync_api import Page
from page.customer_page import CustomerPage

def test_inquiry_cards_count(customer_page: CustomerPage):
    # TC_04: Test number of inquiry card
    customer_page.navigate_to_client()
    customer_page.page.locator('a:has-text("rye")').click()
    inquiry_cards_count = customer_page.get_inquiry_cards_count()
    print(inquiry_cards_count)
    #total_inquiry_count = customer_page.get_total_inquiry_count()
    assert inquiry_cards_count == 36