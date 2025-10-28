import re
from playwright.sync_api import Page,expect,sync_playwright
from pages.HomePage import HomePage
from pages.SearchPage import SearchPage

def test_searchByKeyword(page: Page):
    homePage = HomePage(page)
    searchPage = SearchPage(page)
    page.goto("https://www.ebay.com/") 
    homePage.enterSearchKeyword('iPhone 16')
    homePage.clickSearchBtn()
    value = int (searchPage.getSearchResultCount().replace(',',''))
    assert(value>1000)
    title =  searchPage.getProductDetails()

    with page.context.expect_page() as page_info:
        searchPage.clickFirstSearchResult()  

    new_tab = page_info.value
    new_tab.wait_for_load_state()
    expect(new_tab).to_have_title(re.compile(title+"*"))

def test_searchForKeyword_categoryBased(page:Page):
    homePage = HomePage(page)
    searchPage = SearchPage(page)
    page.goto("https://www.ebay.com/")
    homePage.enterSearchKeyword('soap')
    homePage.clickCategory('baby')
    homePage.clickSearchBtn()
    value = int (searchPage.getSearchResultCount().replace(',',''))
    assert(value>1000)
    title =  searchPage.getProductDetails()

    with page.context.expect_page() as page_info:
        searchPage.clickFirstSearchResult()  

    new_tab = page_info.value
    new_tab.wait_for_load_state()
    expect(new_tab).to_have_title(re.compile(title+"*"))