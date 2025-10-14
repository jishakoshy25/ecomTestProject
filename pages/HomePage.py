from playwright.sync_api import Page

class HomePage:
    def __init__(self,page:Page):
        self.page = page
        self.advancedLink = page.get_by_role('link',name='Advanced')
        self.searchField = page.locator("xpath=//input[@id = 'gh-ac']")
        self.searchButton =  page.locator("css=button#gh-search-btn")
        self.categoryDropdown =  page.locator("xpath=//select[@id = 'gh-cat']")
        self.options = page.locator("xpath=//select[@id = 'gh-cat']/option")
        self.searchCount = page.locator("css=h1.srp-controls__count-heading>span.BOLD:nth-child(1)")

    def clickAdvancedLink(self):
        self.advancedLink.click()

    def enterSearchKeyword(self, keyword:str):
        self.searchField.fill(keyword)

    def clickSearchBtn(self):
        self.searchButton.click()

    def getSearchResultCount(self):
        return self.searchCount.text_content()
    
    def clickLink(self, linkText: str):
        self.page.get_by_role('link',name=linkText).click()
    
    def clickCategory(self, category: str):
        for option in self.options.all_inner_texts():
            if category.lower() in option.lower():
                self.categoryDropdown.select_option(label=option)
                break

        
        
