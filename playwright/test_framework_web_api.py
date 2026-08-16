import json

import pytest
from playwright.sync_api import Playwright, expect

from pageObjects.orderHistoryPage import OrderHistoryPage
from utils.apiBaseFramework import APIUtils
from pageObjects.loginPage import LoginPage

# create JSON file (contain the data) -> util (convert JSON to python obj) -> access into test
with open('playwright/data/credentials.json') as json_file:
    credentials = json.load(json_file)
    user_credential_list = credentials['user_credentials']

@pytest.mark.parametrize('user_credentials', user_credential_list,indirect=True)
def test_e2e_web_api(playwright:Playwright, browserInstance, user_credentials):
    userEmail = user_credentials["userEmail"]
    userPassword = user_credentials["userPassword"]

    #Browser Instance
    #create order -> orderID
    api_Utils = APIUtils()
    order_ID = api_Utils.createOrder(playwright,user_credentials)

    #Login Page
    loginPage = LoginPage(browserInstance) #object for LoginPage class
    loginPage.navigate()

    # Dashboard Page
    dashboardPage = loginPage.login(userEmail,userPassword) #object for DashboardPage class
    orderHistoryPage = dashboardPage.selectOrderNavLink() #object for OrderHistoryPage class
    orderDetailspage = orderHistoryPage.selectOrder(order_ID) #object for OrderDetailPage class
    orderDetailspage.verifyOrder()


