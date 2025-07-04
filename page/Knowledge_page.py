from playwright.sync_api import Page, expect

class KnowledgePage:
    def __init__(self, page: Page):
        self.page = page
        # Locators for file operations
        self.delete_button = page.locator('button:has(svg.lucide-trash2.text-danger)')
        self.download_button = page.locator('button:has(svg.lucide.lucide-cloud-download)')
        self.confirm_button = page.locator('button:has-text("Confirm")')
        self.cancel_button = page.locator('button:has-text("Cancel")')
        self.source_table = page.locator('table')
        self.search_input = page.locator('input[placeholder="Search sources..."]')
        self.table_rows = page.locator('table tr')

    def navigate_to_knowledge(self):
        """Navigate to the knowledge page"""
        self.page.goto("https://cx-call-center-dev.talena.ai/knowledge")
        self.page.wait_for_timeout(2000)

    def get_table_row_count(self) -> int:
        """
        Get the number of rows in the table
        Returns:
            int: Number of rows in the table
        """
        return self.table_rows.count()

    def is_source_visible(self, source_name: str) -> bool:
        """
        Check if a source is visible in the table
        Args:
            source_name (str): Name of the source to check
        Returns:
            bool: True if source is visible, False otherwise
        """
        return self.page.locator(f"text={source_name}").is_visible()

    def click_delete_button(self):
        """Click the delete button"""
        self.delete_button.nth(0).click()
        self.page.wait_for_timeout(2000)

    def click_download_button(self):
        """Click the download button"""
        self.download_button.nth(0).click()

    def click_confirm_button(self):
        """Click the confirm button"""
        self.confirm_button.click()

    def click_cancel_button(self):
        """Click the cancel button"""
        self.cancel_button.click()

    def search_source(self, source_name: str):
        """
        Search for a source
        Args:
            source_name (str): Name of the source to search for
        """
        self.search_input.fill(source_name) 