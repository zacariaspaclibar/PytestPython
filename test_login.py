from playwright.sync_api import Playwright,expect

def test_login_success(playwright:Playwright):
    new_browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = new_browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    page.get_by_label("username").fill("rahulshettyacademy")
    page.get_by_label("password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option(value="teach")
    page.get_by_role("checkbox",name="I Agree to the terms and conditions").click()
    page.get_by_role("button",name="Sign In").click()
    expect(page).to_have_url("https://rahulshettyacademy.com/angularpractice/shop")


