import pytest
from playwright.sync_api import Page
from page.Knowledge_page import KnowledgePage

def test_delete_file_cancel(page: Page, knowledge_page: KnowledgePage):
    
    knowledge_page = KnowledgePage(page)

    # Step 3-4: Cancel delete operation
    knowledge_page.click_delete_button()

    knowledge_page.click_cancel_button()
    
    # Verify the dialog is closed
    assert not knowledge_page.confirm_button.is_visible(), "The dialog should be closed after clicking Cancel" 