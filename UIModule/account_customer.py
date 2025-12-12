# Author:Yi Sun(Tim) 2025-10-30

'''Account Customer Page'''

from playwright.sync_api import Page,expect
from UIModule.admin_portal import Admin_Page

class Account_Customer(Admin_Page):

    def __init__(self,page:Page):
        super().__init__(page)
        self._init_locators_account_customer()

    def _init_locators_account_customer(self):
        '''loc for default values in this page'''
        self.account_title_loc = self.page.locator("[data-test='login-submit']")
        self.account_searchbtn_loc = self.page.locator(".btn.btn-search")
        self.account_searchbox_loc = self.page.locator('#searchCustomerName')    #this is for ID
        self.customer_name_loc = self.page.locator('#customername)
        self.contact_name_loc = self.page.locator("xpath=//div[contains(@class,'cname')]")
        self.address_loc = self.page.locator("[name='address']")
        self.email_loc = self.page.locator("[name='email']")
        self.suburb_loc = self.page.locator("[name='uburb']")
        self.search_result_name_loc = self.page.locator('#searchCustomerResult)

    def goto_account_customer(self):
        '''Go to account customer screen'''
        self.list_loc.click()
        self.account_list_loc.click()
        self.account_title_loc.wait_for()

    @property
    def check_accountcustomer_url(self):
        account_customer_url = self.page.url
        print('url is:',account_customer_url)
        return account_customer_url

    @property
    def check_accountcustomer_title(self):
        '''Check the url'''
        acocount_customer_title = self.account_title_loc.inner_text()
        print('title is:',acocount_customer_title)
        return acocount_customer_title

    @property
    def check_search_btn(self):
        '''Check the search button'''
        account_btn = self.account_searchbtn_loc
        if account_btn.is_enabled():
            print('is there')
            return True
        else:
            print('is missing')
            return False

    @property
    def check_searchbox(self):
        '''Check the search box'''
        account_box = self.account_searchbox_loc
        if account_box.is_visible():
            print('is there')
            return True
        else:
            print('is missing')
            return False

    @property
    def check_columns(self):
        '''Check each column on the screen'''
        customer_name = self.customer_name_loc.inner_text()
        contact_name = self.contact_name_loc.inner_text()
        address = self.address_loc.inner_text()
        email = self.email_loc.inner_text()
        suburb = self.suburb_loc.inner_text()
        print(customer_name,contact_name,address,email,suburb)
        return customer_name,contact_name,address,email,suburb

    @property
    def check_search_result(self):
        '''Check the Search function'''
        self.account_searchbox_loc.fill('tim2')
        # self.page.wait_for_timeout(3000)  # 等待3秒
        self.account_searchbtn_loc.click()

        self.search_result_name_loc.wait_for()
        search_result_name = self.search_result_name_loc.inner_text()
        print(search_result_name)
        return search_result_name


if __name__ == '__main__':
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page(viewport={"width": 2560, "height": 1600})
        page.goto(" ")
        login = Account_Customer(page)
        login.typeUserName('aabb')
        login.typePassword('aabb')
        login.clicklogin()
        page.wait_for_timeout(3000)
        login.goto_account_customer()
        # login.check_accountcustomer_url
        # login.check_accountcustomer_title
        # login.check_search_btn
        # login.check_searchbox
        # login.check_columns
        login.check_search_result



