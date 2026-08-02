from playwright.sync_api import Page
import utils.credentials

fakePayloadOrderResponse = {"data":[],"message":"No Orders"}
# api call from browser
# -> api call contact server return back response [intercept response -> giving the route fulfill] to browser
# -> browser use response to generate the data / HTML

def intercept_response(route):
    route.fulfill(
        json = fakePayloadOrderResponse
    )

def test_Network1(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_role("textbox", name="email@example.com").fill(utils.credentials.USERNAME)
    page.get_by_role("textbox", name="enter your passsword").fill(utils.credentials.PASSWORD)
    page.get_by_role("button", name="Login").click()
    page.get_by_role('button', name='  ORDERS').click()

    order_text = page.get_by_text('You have No Orders to show at this time. Please Visit Back Us').text_content()
    print(order_text)