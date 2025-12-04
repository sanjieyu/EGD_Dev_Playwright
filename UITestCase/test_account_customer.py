# Author:Yi Sun(Tim) 2025-10-31

'''Test Account Customer Page by Unittest'''
import unittest
from playwright.sync_api import sync_playwright,expect
from UIModule.account_customer import Account_Customer
from CommomModule.read_config import *


class TestAccountCustomer(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.firefox.launch(headless=False)
        cls.page = cls.browser.new_page(viewport={"width": 2560, "height": 1600})

        cls.config_read = ReadConfig()
        cls.url = cls.config_read.get_url()
        cls.admin_username = cls.config_read.admin_username()
        cls.admin_password = cls.config_read.admin_password()
        cls.account_customer = Account_Customer(cls.page)
        cls.page.goto(cls.url)
        cls.account_customer.typeUserName(cls.admin_username)
        cls.account_customer.typePassword(cls.admin_password)
        cls.account_customer.clicklogin()
        cls.account_customer.goto_account_customer()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.page.close()
        cls.browser.close()
        cls.playwright.stop()

    def test_account_customer_ui_001(self):
        '''Verify the url'''
        current_url = self.account_customer.check_accountcustomer_url
        self.assertEqual("http://aabb/List",current_url)

    def test_account_customer_ui_002(self):
        '''Verify the title'''
        self.assertEqual('Account Customers Search',self.account_customer.check_accountcustomer_title)

    def test_account_customer_ui_003(self):
        '''Verify the search button'''
        self.assertTrue(self.account_customer.check_search_btn)

    def test_account_customer_ui_004(self):
        '''Verify the search box'''
        self.assertTrue(self.account_customer.check_searchbox)

    def test_account_customer_ui_005(self):
        '''Verify each column on this screen'''
        self.assertEqual(('Customer Name','Contact Name','Address','Email','Suburb'),
                         self.account_customer.check_columns)


if __name__ == "__main__":
    unittest.main(verbosity=2)
