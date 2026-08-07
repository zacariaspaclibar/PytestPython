from playwright.sync_api import expect


class OrderDetailsPage:
    def __init__(self,page):
        self.page = page

    def verifyOrder(self):
        expect(self.page.locator('body')).to_contain_text('order summary')