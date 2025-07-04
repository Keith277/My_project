import pytest
from playwright.sync_api import Page
from page.Knowledge_page import KnowledgePage
from page.login_page import LoginPage

def test_download_file_successfully(page: Page, knowledge_page: KnowledgePage):
    
    # Step 2: Navigate to knowledge page
    knowledge_page = KnowledgePage(page)
    knowledge_page.navigate_to_knowledge()
    
    # Step 3-4: Download file
    knowledge_page.click_download_button()
    knowledge_page.click_confirm_button()
    
    # Note: In a real scenario, you would want to verify the download
    # This could be done by checking the downloads directory or network requests
    # For now, we'll just verify the dialog is closed
    assert not knowledge_page.confirm_button.is_visible(), "The download dialog should be closed after confirmation" 