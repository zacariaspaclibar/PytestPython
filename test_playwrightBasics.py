import pytest
from playwright.sync_api import Page, expect


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com")

def test_playwrightFirefox(playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com")

def test_playwrightShortcut(page:Page):
    page.goto("https://www.google.com")

def test_coreLocator(page:Page):
    page.goto("https://www.google.com")
