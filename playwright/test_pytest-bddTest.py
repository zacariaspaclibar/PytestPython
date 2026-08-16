import pytest
from pytest_bdd import scenario, given, when, then, parsers, scenarios
from playwright.sync_api import Playwright

from pageObjects.loginPage import LoginPage
from utils.apiBaseFramework import APIUtils

scenarios('features/orderTransaction.feature')

@pytest.fixture
def shared_data():
    return {}

@given(parsers.parse('place item order with {username} and {password}'))
def placeItemOrder(playwright:Playwright,username,password,shared_data):
    user_credentials = {}
    user_credentials["userEmail"] = username
    user_credentials["userPassword"] = password

    api_Utils = APIUtils()
    order_ID = api_Utils.createOrder(playwright, user_credentials)
    shared_data['order_id'] = order_ID

@given('the user is on landing page')
def user_on_landing_page(browserInstance,shared_data):
    loginPage = LoginPage(browserInstance)  # object for LoginPage class
    loginPage.navigate()
    shared_data['login_page'] = loginPage

@when(parsers.parse('I login to portal with {username} and {password}'))
def login_to_portal(username,password,shared_data):
    loginPage = shared_data['login_page']
    dashboardPage = loginPage.login(username, password)
    shared_data['dashboardPage'] = dashboardPage

@when('navigate to orders page')
def navigate_to_orders_page(shared_data):
    dashboardPage = shared_data['dashboardPage']
    orderHistoryPage = dashboardPage.selectOrderNavLink()
    shared_data['orderHistoryPage'] = orderHistoryPage

@when('select the orderId')
def select_the_order_id(shared_data):
    order_ID = shared_data['order_id']
    orderHistoryPage = shared_data['orderHistoryPage']
    orderDetailspage = orderHistoryPage.selectOrder(order_ID)
    shared_data['orderDetailspage'] = orderDetailspage

@then('order message is successfully displayed')
def order_successfully(shared_data):
    orderDetailspage = shared_data['orderDetailspage']
    orderDetailspage.verifyOrder()

