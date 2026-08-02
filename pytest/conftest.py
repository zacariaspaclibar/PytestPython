import pytest
from playwright.sync_api import Playwright

@pytest.fixture(scope="session")
def browser_chromium(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

@pytest.fixture(scope="session")
def browser_firefox(playwright:Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()


