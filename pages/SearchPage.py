from playwright.sync_api import Page

class SearchPage:
    def __init__(self,page:Page):
        self.page = page
        self.searchCount = page.locator("css=h1.srp-controls__count-heading>span.BOLD:nth-child(1)")
        self.searchResult =  page.locator("ul.srp-results>li").first
        self.productLink = page.locator('ul.srp-results>li a.su-link span').first

    def getSearchResultCount(self):
        return self.searchCount.text_content()
    
    def clickFirstSearchResult(self):
        self.productLink.click(force=True)

    def getProductDetails(self):
        return self.productLink.text_content()