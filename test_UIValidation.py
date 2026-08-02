from playwright.sync_api import Playwright,expect



def test_childWindowhandle(playwright:Playwright):
    new_browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = new_browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as newPage:
        page.get_by_role("link",name="Free Access to InterviewQues/ResumeAssistance/Material").click()
        child_Page = newPage.value
        text = child_Page.locator(".red").text_content()
        word = text.split("at")
        email = word[1].split(" ")[1]
        assert email == "mentor@rahulshettyacademy.com"