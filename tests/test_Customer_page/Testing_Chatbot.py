import pytest
from playwright.sync_api import Page
from page.customer_page import CustomerPage

def test_chatbot(customer_page: CustomerPage):
    # TC_06: Testing Chatbot
    customer_page.page.locator('text=Knowledge Management').click()
    customer_page.test_chatbot("かぐわしき八ッ橋が在庫中ですか？")
    assert customer_page.page.locator("text=かぐわしき八ッ橋が在庫中ですか？").is_visible() 