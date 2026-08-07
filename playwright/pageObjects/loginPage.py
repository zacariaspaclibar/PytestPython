from pageObjects.dashboardpage import DashboardPage


class LoginPage:
    def __init__(self,page):
        self.page = page

    def navigate(self):
        self.page.goto('https://rahulshettyacademy.com/client')

    def login(self,userEmail,userPassword):
        self.page.get_by_role("textbox", name="email@example.com").fill(userEmail)
        self.page.get_by_role("textbox", name="enter your passsword").fill(userPassword)
        self.page.get_by_role("button", name="Login").click()

        dashboardPage = DashboardPage(self.page)
        return dashboardPage