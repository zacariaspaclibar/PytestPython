import json

import pytest
from playwright.sync_api import Playwright, expect
from utils.apiBase import APIUtils
import utils.credentials

# create JSON file (contain the data) -> util (convert JSON to python obj) -> access into test
with open('data/credentials.json') as json_file:
    credentials = json.load(json_file)
    user_credential_list = credentials['user_credentials']
    print(f"user credential list: {user_credential_list}")

@pytest.mark.parametrize('user_credentials', user_credential_list, indirect=True)
def test_e2e_web_api(playwright:Playwright, user_credentials):
    print(f'Inside the test case: {user_credentials}')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()


    #create order -> orderID
    api_Utils = APIUtils()
    order_ID = api_Utils.createOrder(playwright)


    #Login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("textbox", name="email@example.com").fill(user_credentials["userEmail"])
    page.get_by_role("textbox", name="enter your passsword").fill(user_credentials["userPassword"])
    page.get_by_role("button", name="Login").click()


    #order History page -> order is present
    page.get_by_role('button', name='  ORDERS').click()

    page.locator('tr').filter(has_text=order_ID).get_by_role('button',name='View').click()
    expect(page.locator('body')).to_contain_text('order summary')
    context.close()

