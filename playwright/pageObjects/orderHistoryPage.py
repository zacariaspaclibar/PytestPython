from pageObjects.orderDetailsPage import OrderDetailsPage


class OrderHistoryPage:
    def __init__(self,page):
        self.page = page

    def selectOrder(self,order_ID):
        self.page.locator('tr').filter(has_text=order_ID).get_by_role('button', name='View').click()
        orderDeatilspage = OrderDetailsPage(self.page)
        return orderDeatilspage
