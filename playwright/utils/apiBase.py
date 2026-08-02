from playwright.sync_api import Playwright
import utils.credentials

ordersPayLoad = {"orders":[{"country":"Philippines","productOrderedId":"6960eae1c941646b7a8b3ed3"}]}
getTokenPayload = {"userEmail":utils.credentials.USERNAME,"userPassword":utils.credentials.PASSWORD}

class APIUtils:
    # create a token -> calling the api endpoint login to generate a token
    def getToken(self,playwright:Playwright):
        api_request_context = playwright.request.new_context(base_url='https://rahulshettyacademy.com')
        response = api_request_context.post(url='api/ecom/auth/login',
                                 data=getTokenPayload)
        assert response.ok
        responseBody = response.json()
        return responseBody['token']

    # this function is for creating an order using the API endpoint - orderCreate
    def createOrder(self,playwright:Playwright):
        token = self.getToken(playwright)
        api_request_context = playwright.request.new_context(base_url='https://rahulshettyacademy.com')
        response = api_request_context.post(url='api/ecom/order/create-order',
                                 data=ordersPayLoad,
                                 headers={'Content-Type':'application/json',
                                                             'Authorization': token})
        response_body = response.json()
        order_ID =response_body['orders'][0]
        return order_ID

