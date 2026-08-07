from pageObjects.orderHistoryPage import OrderHistoryPage


class DashboardPage:
    def __init__(self,page):
        self.page = page

    def selectOrderNavLink(self):
        # order History page -> order is present
        self.page.get_by_role('button', name='  ORDERS').click()
        orderHistoryPage = OrderHistoryPage(self.page)
        return orderHistoryPage