# Author:Yi Sun(Tim) 2025-10-28

'''Admin Portal Page'''

from playwright.sync_api import Page,expect
from UIModule.login_admin import Admin_Portal

class Admin_Page(Admin_Portal):

    def __init__(self,page:Page):
        super().__init__(page)
        self.page = page
        self._init_locators()

    def _init_locators(self):
        '''loc for default values in this page'''
        self.eco_icon_loc = self.page.locator('xpath=/html/body/div[2]/div/div[1]/a/img')
        self.add_loc = self.page.locator('xpath=/html/body/div[2]/div/div[2]/ul/li[1]/a')
        self.list_loc = self.page.locator('xpath=/html/body/div[2]/div/div[2]/ul/li[2]/a')
        self.findquote_box_loc = self.page.locator('#search-quote')
        self.findquote_button_loc = self.page.locator('xpath=/html/body/div[2]/div/div[2]/div[1]/div/div/button')
        self.findaddress_box_loc = self.page.locator('#search-address')
        self.findaddress_button_loc = self.page.locator('xpath=/html/body/div[2]/div/div[2]/div[2]/div/div/button')
        self.findclient_box_loc = self.page.locator('#search-client')
        self.findclient_button_loc = self.page.locator('xpath=//*[@id="search-client-btn"]')
        self.account_loc = self.page.locator('xpath=/html/body/div[2]/div/div[2]/form/ul/li/a')
        self.copyright_loc = self.page.locator('xpath=/html/body/footer/div/p')
        self.terms_loc = self.page.locator('xpath=/html/body/footer/div/a')

        # 保存选择器字符串用于 wait_for_selector
        self.copyright_selector = 'xpath=/html/body/footer/div/p'

        '''Add Menu'''
        self.quote_add_loc = self.page.locator('xpath=/html/body/div[2]/div/div[2]/ul/li[1]/ul/li[1]/a')
        self.lead_add_loc = self.page.locator('xpath=/html/body/div[2]/div/div[2]/ul/li[1]/ul/li[2]/a')
        self.account_add_loc = self.page.locator('xpath=/html/body/div[2]/div/div[2]/ul/li[1]/ul/li[3]/a')
        self.installer_add_loc = self.page.locator('xpath=/html/body/div[2]/div/div[2]/ul/li[1]/ul/li[4]/a')

        '''List Menu'''
        self.quote_list_loc = self.page.locator('xpath=/html/body/div[2]/div/div[2]/ul/li[2]/ul/li[1]/a')
        self.services_list_loc = self.page.locator('xpath=/html/body/div[2]/div/div[2]/ul/li[2]/ul/li[2]/a')
        self.account_list_loc = self.page.locator('xpath=/html/body/div[2]/div/div[2]/ul/li[2]/ul/li[3]/a')
        self.report_list_loc = self.page.locator('xpath=/html/body/div[2]/div/div[2]/ul/li[2]/ul/li[4]/a')
        self.installer_list_loc = self.page.locator('xpath=/html/body/div[2]/div/div[2]/ul/li[2]/ul/li[5]/a')
        self.myob_list_loc = self.page.locator('xpath=/html/body/div[2]/div/div[2]/ul/li[2]/ul/li[6]/a')
        self.jobaccept_list_loc = self.page.locator('xpath=/html/body/div[2]/div/div[2]/ul/li[2]/ul/li[7]/a')
        self.onhold_list_loc = self.page.locator('xpath=/html/body/div[2]/div/div[2]/ul/li[2]/ul/li[8]/a')
        self.neworder_list_loc = self.page.locator('xpath=/html/body/div[2]/div/div[2]/ul/li[2]/ul/li[9]/a')
        self.production_list_loc = self.page.locator('xpath=/html/body/div[2]/div/div[2]/ul/li[2]/ul/li[10]/a')
        self.productionWA_list_loc = self.page.locator('xpath=/html/body/div[2]/div/div[2]/ul/li[2]/ul/li[11]/a')
        self.schedule_list_loc = self.page.locator('xpath=/html/body/div[2]/div/div[2]/ul/li[2]/ul/li[12]/a')
        self.pipeline_list_loc = self.page.locator('xpath=/html/body/div[2]/div/div[2]/ul/li[2]/ul/li[13]/a')
        self.activepipeline_list_loc = self.page.locator('xpath=/html/body/div[2]/div/div[2]/ul/li[2]/ul/li[14]/a')

        '''Account Menu'''
        self.changepwd_loc = self.page.locator('xpath=/html/body/div[2]/div/div[2]/form/ul/li/ul/li[3]/a')
        self.updateprofile_loc = self.page.locator('xpath=/html/body/div[2]/div/div[2]/form/ul/li/ul/li[4]/a')
        self.updateemail_loc = self.page.locator('xpath=/html/body/div[2]/div/div[2]/form/ul/li/ul/li[5]/a')
        self.usermanage_loc = self.page.locator('xpath=/html/body/div[2]/div/div[2]/form/ul/li/ul/li[7]/a')
        self.travel_area_loc = self.page.locator('xpath=/html/body/div[2]/div/div[2]/form/ul/li/ul/li[9]/a')
        self.rollcycle_loc = self.page.locator('xpath=/html/body/div[2]/div/div[2]/form/ul/li/ul/li[10]/a')
        self.rollcycle_panellift_loc = self.page.locator(
            'xpath=/html/body/div[2]/div/div[2]/form/ul/li/ul/li[10]/ul/li[1]/a')
        self.rollcycle_rollerdoors_loc = self.page.locator(
            'xpath=/html/body/div[2]/div/div[2]/form/ul/li/ul/li[10]/ul/li[2]/a')
        self.rollcycle_optiliftdoors_loc = self.page.locator(
            'xpath=/html/body/div[2]/div/div[2]/form/ul/li/ul/li[10]/ul/li[3]/a')
        self.sms_loc = self.page.locator('xpath=/html/body/div[2]/div/div[2]/form/ul/li/ul/li[11]/a')
        self.logoff_loc = self.page.locator('xpath=/html/body/div[2]/div/div[2]/form/ul/li/ul/li[13]/a')


    @property
    def getURL(self):
        '''get the url of Admin login portal'''
        self.copyright_loc.wait_for()
        print('url is:',self.page.url)
        return self.page.url

    @property
    def check_defaultmenu(self):
        '''check the default values in Admin Login page'''
        add_menu = self.add_loc.inner_text().strip()
        list_menu = self.list_loc.inner_text().strip()
        account_menu = self.account_loc.inner_text().strip()
        print(add_menu,list_menu,account_menu)
        return add_menu,list_menu,account_menu

    @property
    def check_findquote(self):
        if self.findquote_box_loc.is_visible():
            print('true')
            return True
        else:
            return False

    @property
    def check_findclient(self):
        '''check the Find Client in Admin Login page'''
        if self.findclient_box_loc.is_visible():
            print('true')
            return True
        else:
            return False

    @property
    def add_menu(self):
        self.add_loc.click()
        quote_add = self.quote_add_loc.inner_text().strip()
        lead_add = self.lead_add_loc.inner_text().strip()
        account_add = self.account_add_loc.inner_text().strip()
        install_add = self.installer_add_loc.inner_text().strip()
        print(quote_add,lead_add,account_add,install_add)
        return quote_add,lead_add,account_add,install_add

    @property
    def check_copyright(self):
        copyright = self.copyright_loc.text_content().strip()
        terms = self.terms_loc.text_content().strip()
        print(copyright,terms)
        return copyright,terms


if __name__ == '__main__':
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page(viewport={"width": 2560, "height": 1440})
        page.goto("http:// ")
        login = Admin_Page(page)
        login.typeUserName('aabb')
        login.typePassword('aabb')
        login.clicklogin()
        page.wait_for_timeout(3000)
        # 执行测试
        login.getURL
        # login.check_defaultmenu
        # login.check_findquote
        login.check_copyright


