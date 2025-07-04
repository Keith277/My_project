import pytest
from playwright.sync_api import Page
from page.Knowledge_page import KnowledgePage
from page.login_page import LoginPage

@pytest.fixture
def knowledge_page(page: Page) -> KnowledgePage:
    # Login first
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login("admin@gmail.com", "123456aA@")
    
    # Create knowledge page
    knowledge_page = KnowledgePage(page)
    knowledge_page.navigate_to_knowledge()
    return knowledge_page 