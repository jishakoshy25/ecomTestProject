from playwright.sync_api import Page

class AdvancedSearch:
    def __init__(self, page: Page):
        self.page = page
        self.ebayLogo =  page.locator('a.gh-logo')
        self.keywordField = page.get_by_label('Enter keywords or item number')
        self.exclude = page.get_by_label('Exclude words from your search')
        self.minPrice = page.locator('//input[@name="_udlo"]')
        self.maxPrice =  page.locator('//input[@name="_udhi"]')
        self.searchBtn =  page.locator('div.adv-form__actions >button.btn.btn--primary' )

    def clickEbayLogo(self):
        self.ebayLogo.click()
    
    def enterKeyword(self, keyword: str):
        self.keywordField.fill(keyword)

    def enterExcludeCriteria(self, excludeText: str):
        self.exclude.fill(excludeText)
    
    def enterMinPrice(self, minPrice: str):
        self.minPrice.fill(minPrice)

    def enterMaxPrice(self, maxPrice: str):
        self.maxPrice.fill(maxPrice)
    
    def clickSearchBtn(self):
        self.searchBtn.click()