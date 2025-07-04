import pytest
from playwright.sync_api import Page
from page.Knowledge_page import KnowledgePage
from page.login_page import LoginPage

def test_download_file_cancel(page: Page, knowledge_page: KnowledgePage):
    
    
    # Step 2: Navigate to knowledge page
    knowledge_page = KnowledgePage(page)
    
    # Step 3-4: Cancel download operation
    knowledge_page.click_download_button()
    knowledge_page.click_cancel_button()
    
    # Verify the dialog is closed
    assert not knowledge_page.confirm_button.is_visible(), "The download dialog should be closed after clicking Cancel" 