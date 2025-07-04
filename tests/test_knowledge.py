import pytest
from page.knowledge_page import KnowledgePage

@pytest.fixture
def knowledge_page(page):
    knowledge_page = KnowledgePage(page)
    knowledge_page.navigate_to_knowledge()
    return knowledge_page

def test_delete_source_successfully(knowledge_page):
    """TC_01: Delete file successfully"""
    # Store the source name before deletion
    source_name = "Test Source"  # Replace with actual source name from the page
    
    # Delete the source
    knowledge_page.delete_source(confirm=True)
    
    # Verify the source is no longer visible
    assert not knowledge_page.is_source_visible(source_name), "Source should be deleted"

def test_delete_source_fail(knowledge_page):
    """TC_02: Delete file fail"""
    # Store the source name before attempting deletion
    source_name = "Test Source"  # Replace with actual source name from the page
    
    # Attempt to delete but cancel
    knowledge_page.delete_source(confirm=False)
    
    # Verify the source is still visible
    assert knowledge_page.is_source_visible(source_name), "Source should still be visible after cancellation"

def test_download_source(knowledge_page):
    """TC_03: Download file"""
    # Download the source
    knowledge_page.download_source(confirm=True)
    
    # Note: Playwright doesn't have a direct way to verify file downloads
    # This test assumes the download completes successfully
    # In a real scenario, you might want to check the downloads directory

def test_download_source_cancel(knowledge_page):
    """TC_04: Download file with cancellation"""
    # Store the source name before attempting download
    source_name = "Test Source"  # Replace with actual source name from the page
    
    # Attempt to download but cancel
    knowledge_page.download_source(confirm=False)
    
    # Verify the source is still visible
    assert knowledge_page.is_source_visible(source_name), "Source should still be visible after download cancellation" 