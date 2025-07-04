from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator('input[name="email"]')
        self.password_input = page.locator('input[name="password"]')
        self.error_message = page.locator("text=Invalid email, Invalid password")

    def navigate_to_login(self):
        self.page.goto("https://cx-call-center-dev.talena.ai/auth/login")

    def login(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.page.wait_for_timeout(1500)
        self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(3000)

    def is_error_message_visible(self, message: str) -> bool:
        return self.page.locator(f"text={message}").is_visible()

    def is_on_client_page(self) -> bool:
        return self.page.url == "https://cx-call-center-dev.talena.ai/client" 