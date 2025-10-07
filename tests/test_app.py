import re
from playwright.sync_api import Page,expect
from pages.HomePage import HomePage

def test_pageTitle(page: Page):
    page.goto("https://www.ebay.com/")
    expect(page).to_have_title(re.compile("eBay"))

def test_links(page:Page):
    homePage = HomePage(page)
    page.goto("https://www.ebay.com/")
    homePage.clickLink('Motors')
    expect(page).to_have_url(re.compile("https://www.ebay.com/b/Auto-Parts-and-Vehicles/*"))
    expect(page).to_have_title(re.compile("eBay Motors*"))

def test_advancedLinkCheck(page:Page):
    homePage = HomePage(page)
    page.goto("https://www.ebay.com/")
    homePage.clickAdvancedLink()
    expect(page).to_have_title(re.compile("Advanced Search*"))
    expect(page).to_have_url(re.compile("https://www.ebay.com/sch/ebayadvsearch"))

    