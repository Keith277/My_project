import pytest
from playwright.sync_api import Page
from page.customer_page import CustomerPage

def test_customer_detail(customer_page: CustomerPage):
    # TC_03: Test customer detail
    customer_page.click_customer_link("rye")
    assert customer_page.page.url == "https://cx-call-center-dev.talena.ai/inquiry-history/7311293904849117185"
    info_container = customer_page.page.locator("div.mt-3.flex.flex-col.items-start")

    # Lấy toàn bộ text trong vùng này
    container_text = info_container.text_content()

    # Danh sách label cần kiểm tra
    expected_labels = ["Client ID", "Phone", "Inquiry", "Last Inquiry Date"]

    # Duyệt từng label và assert xem có nằm trong text hay không
    for label in expected_labels:
        assert label in container_text, f"'{label}' not found in customer detail block"