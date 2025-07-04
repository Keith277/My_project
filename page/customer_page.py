from playwright.sync_api import Page, expect

class CustomerPage:
    def __init__(self, page: Page):
        self.page = page
        self.customer_detail = page.locator('div.mt-3.flex.flex-col.items-start')
        self.search_bar = page.locator('input[placeholder="Search for customer, phone number,..."]')
        self.inquiry_section = page.locator('div.flex.flex-1.basis-0.flex-col.gap-3.overflow-auto')
        self.inquiry_cards = page.locator('div.flex.flex-1.basis-0.flex-col.gap-3.overflow-auto a')
        self.total_inquiry = page.locator('span.text-sm.font-medium.text-gray-900')
        self.conversation_section = page.locator('div.flex.flex-1.basis-0.flex-col.gap-4.overflow-auto')
        self.test_chatbot_btn = page.locator('text=Test Chatbot')
        self.start_chat_btn = page.locator('text=Start Chat')
        self.chat_bar = page.locator('input[placeholder="Chat with Mochi"]')
        self.add_source_btn = page.locator('text=Add Source')
        self.source_name_input = page.locator('input[placeholder="Enter source name"]')
        self.add_source_submit_btn = page.locator("button[type='submit']")
        self.add_customer_button = page.locator('button:has-text("Add Customer")')
        self.customer_name_input = page.locator('input[name="customerName"]')
        self.customer_email_input = page.locator('input[name="customerEmail"]')
        self.customer_phone_input = page.locator('input[name="customerPhone"]')
        self.save_button = page.locator('button:has-text("Save")')
        self.cancel_button = page.locator('button:has-text("Cancel")')
        self.customer_table = page.locator('table')
        self.search_input = page.locator('input[placeholder="Search customers..."]')
        self.edit_button = page.locator('button:has-text("Edit")')
        self.delete_button = page.locator('button:has-text("Delete")')

    def navigate_to_client(self):
        self.page.goto("https://cx-call-center-dev.talena.ai/client")

    def check_table(self):
        self.page.locator('text=Customer').is_visible()
        self.page.locator('text=Customer ID').is_visible()
        self.page.locator('text=Phone Number').is_visible()
        self.page.locator('text=Inquiry').is_visible()
        self.page.locator('text=Last Inquiry Date').is_visible()

    def search_customer(self, search_term: str):
        self.search_bar.fill(search_term)
        self.page.wait_for_timeout(1000)

    def click_customer_link(self, customer_name: str):
        self.page.locator(f'text={customer_name}').click()
        self.page.wait_for_timeout(15000)

    def get_inquiry_cards_count(self) -> int:
        return self.inquiry_cards.count()

    def get_total_inquiry_count(self) -> int:
        return int(self.total_inquiry.text_content())
        self.page.wait_for_timeout(1000)

    def click_inquiry_card(self, index: int):
        self.inquiry_cards.nth(index).click()
        self.page.wait_for_timeout(10000)

    def get_conversation_content(self) -> str:
        return self.conversation_section.text_content()

    def test_chatbot(self, message: str):
        self.test_chatbot_btn.click()
        self.start_chat_btn.click()
        self.page.wait_for_timeout(10000)
        self.chat_bar.fill(message)
        self.page.keyboard.press("Enter")

    def add_source(self, source_name: str, file_path: str = None):
        self.add_source_btn.click()
        if source_name:
            self.source_name_input.fill(source_name)
        if file_path:
            self.page.locator('input[type="file"]').set_input_files(file_path)
        self.add_source_submit_btn.click()

    def is_error_message_visible(self, message: str) -> bool:
        return self.page.locator(f"text={message}").is_visible()

    def is_on_knowledge_page(self) -> bool:
        return self.page.url == "https://cx-call-center-dev.talena.ai/knowledge"

    def navigate_to_customers(self):
        self.page.goto("https://cx-call-center-dev.talena.ai/customers")

    def add_customer(self, name: str, email: str, phone: str):
        self.add_customer_button.click()
        self.customer_name_input.fill(name)
        self.customer_email_input.fill(email)
        self.customer_phone_input.fill(phone)
        self.save_button.click()

    def edit_customer(self, old_name: str, new_name: str, new_email: str, new_phone: str):
        self.search_input.fill(old_name)
        self.edit_button.click()
        self.customer_name_input.fill(new_name)
        self.customer_email_input.fill(new_email)
        self.customer_phone_input.fill(new_phone)
        self.save_button.click()

    def delete_customer(self, name: str):
        self.search_input.fill(name)
        self.delete_button.click()
        self.save_button.click()  # Confirm deletion

    def is_customer_visible(self, name: str) -> bool:
        return self.page.locator(f"text={name}").is_visible()

    def cancel_customer_operation(self):
        self.cancel_button.click() 