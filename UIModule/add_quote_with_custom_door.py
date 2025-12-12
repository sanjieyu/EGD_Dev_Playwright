# Author:Yi Sun(Tim) 2025-11-26

'''Add a Quote with a Custom  door functio'''

from playwright.sync_api import Page,expect
from UIModule.add_custom_door import Add_Custom_Door
from UIModule.add_quote import Add_Quote

class Add_Quote_With_CustomDoor(Add_Custom_Door):

    def __init__(self,page):
        super().__init__(page)
        self._init_locators_add_quote_with_custom()
        self.add_quote = Add_Quote(page)
        self.add_custom_door = Add_Custom_Door(page)

    def _init_locators_add_quote_with_custom(self):
        self.proposal_number_loc = self.page.locator('#ProposalNo')  # get the proposal number for the edit box
        self.find_quote_input = self.page.locator( '#search-quote')
        self.find_quote_btn = self.page.locator( '#search-btn')

        self.searched_proposal_no_loc = self.page.locator("[name='searchedid']")
        self.searched_door_no_loc = self.page.locator("[name='doorid']")
        self.searched_door_status_loc = self.page.locator("[name='doorstatus']")

    def add_custom_door_fun(self):
        self.add_quote.go_addquote()
        self.add_custom_door.go_addcustomdoor()
        self.add_custom_door.add_custom_detail()
        self.page.wait_for_timeout(2000)
        self.add_quote.check_add_quote_success

    @property
    def get_proposal_number(self):
        global proposal_number
        proposal_number = self.proposal_number_loc.input_value(timeout=3000)
        print('number is:', proposal_number)
        return proposal_number

    def search_new_quote(self):
        self.page.reload()
        self.page.wait_for_timeout(1000)
        self.find_quote_input.fill(proposal_number)
        self.page.wait_for_timeout(2000)
        self.find_quote_btn.click()

    @property
    def verify_new_quote(self):
        searched_proposal_no = self.searched_proposal_no_loc.inner_text(timeout=10000)
        searched_door_no = self.searched_door_no_loc.inner_text(timeout=10000)
        searched_door_status = self.searched_door_status_loc.inner_text(timeout=10000)
        print(searched_door_no,searched_door_status)
        return searched_door_no,searched_door_status


if __name__ == "__main__":
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page(viewport={"width": 2560, "height": 1440})
        # page = browser.new_page()
        page.goto("http:// ")
        login = Add_Quote_With_CustomDoor(page)
        login.typeUserName('aabb')
        login.typePassword('aabb')
        login.clicklogin()
        page.wait_for_timeout(3000)
        login.add_custom_door_fun()
        login.get_proposal_number
        login.search_new_quote()
        login.verify_new_quote


