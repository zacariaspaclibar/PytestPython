from playwright.sync_api import Playwright, expect
from utils.apiBase import APIUtils
import utils.credentials


def test_e2e_web_api(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")

    #create order -> orderID
    api_Utils = APIUtils()
    order_ID = api_Utils.createOrder(playwright)


    #Login
    page.get_by_role("textbox", name="email@example.com").fill(utils.credentials.USERNAME)
    page.get_by_role("textbox", name="enter your passsword").fill(utils.credentials.PASSWORD)
    page.get_by_role("button", name="Login").click()


    #order History page -> order is present
    page.get_by_role('button', name='  ORDERS').click()

    page.locator('tr').filter(has_text=order_ID).get_by_role('button',name='View').click()
    expect(page.locator('body')).to_contain_text('order summary')
    context.close()

