import pytest
from playwright.sync_api import Page
from page.Knowledge_page import KnowledgePage
from page.login_page import LoginPage

def test_delete_file_successfully(knowledge_page: KnowledgePage):
    
    # Step 1: Get initial table row count
    initial_row_count = knowledge_page.get_table_row_count()
    
    # Step 2-3: Delete file
    knowledge_page.click_delete_button()
    knowledge_page.click_confirm_button()
    
    # Wait for the table to update
    knowledge_page.page.wait_for_timeout(2000)
    
    # Get final table row count
    final_row_count = knowledge_page.get_table_row_count()
    print(final_row_count)
    
    # Verify the file is deleted and row count decreased by 1
    assert final_row_count == initial_row_count - 1, f"Table row count should decrease by 1 (was {initial_row_count}, now {final_row_count})" 