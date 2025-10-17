import re
from playwright.sync_api import Page,expect
from pages.AdvancedSearch import AdvancedSearch  

def test_pageTitle(page: Page):
    page.goto("https://www.ebay.com/sch/ebayadvsearch")
    expect(page).to_have_title(re.compile("Advanced Search"))

def test_ebayLogo(page: Page):
    advancedSearchPage =  AdvancedSearch(page)
    page.goto("https://www.ebay.com/sch/ebayadvsearch")
    advancedSearchPage.clickEbayLogo()
    expect(page).to_have_title(re.compile("eBay"))
    expect(page).to_have_url('https://www.ebay.com/')

def test_advancedSearch(page: Page):
    advancedSearchPage =  AdvancedSearch(page)
    page.goto("https://www.ebay.com/sch/ebayadvsearch")
    advancedSearchPage.enterKeyword('iPhone 11')
    advancedSearchPage.enterExcludeCriteria('refurbished')
    advancedSearchPage.enterMinPrice('300')
    advancedSearchPage.enterMaxPrice('900')
    advancedSearchPage.clickSearchBtn()
    expect(page).to_have_url(re.compile('https://www.ebay.com/sch/i.html'))
    expect(page).to_have_title(re.compile(r'iPhone 11'))