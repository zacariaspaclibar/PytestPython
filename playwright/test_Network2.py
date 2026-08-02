from multiprocessing import context

from playwright.sync_api import Page, expect, Playwright
from pytest_playwright.pytest_playwright import browser

import utils.credentials
from utils.apiBase import APIUtils


# api call from the browser [Intercept the request before it reach the server]
# -> [continue the request call to the server with the new URL] api call contact server return back response [intercept response -> giving the route fulfill] to browser
# -> browser use response to generate the data / HTML

def intercept_request(route):
    route.continue_(url='https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6a6ade4d85b8849b491bb08d')


def test_Network2(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    page.get_by_role("textbox", name="email@example.com").fill(utils.credentials.USERNAME)
    page.get_by_role("textbox", name="enter your passsword").fill(utils.credentials.PASSWORD)
    page.get_by_role("button", name="Login").click()
    page.get_by_role('button', name='  ORDERS').click()

    page.locator('tr').filter(has_text='6a6ae2ca85b8849b491bbe03').get_by_role('button',name='View').click()
    expect(page).to_have_url('https://rahulshettyacademy.com/client/#/dashboard/order-details/6a6ae2ca85b8849b491bbe03')
    print('Order Summary page')


def test_session_strorage(playwright:Playwright):
    api_utils = APIUtils()
    getToken = api_utils.getToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # bypass login -> dashboard -> click order -> Verify the Your Order text in the page
    # script to inject token in session local storage
    page.add_init_script(f"""localStorage.setItem('token','{getToken}')""")
    page.goto("https://rahulshettyacademy.com/client/#/dashboard/dash")
    page.get_by_role('button', name='ORDERS').click()
    expect(page.get_by_role('heading',name='Your Orders')).to_be_visible()


