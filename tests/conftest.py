import pytest
from playwright.sync_api import sync_playwright, Page

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=1000
        )
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser) -> Page:
    page = browser.new_page()
    yield page
    page.close() 