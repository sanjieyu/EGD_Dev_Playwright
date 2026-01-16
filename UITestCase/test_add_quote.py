# Author:Yi Sun(Tim) 2025-11-06

'''Test Add Quote Page'''

import unittest
from playwright.sync_api import sync_playwright,expect
from UIModule.add_quote import Add_Quote
from CommomModule.read_config import *

class TestAddQuote(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.firefox.launch(headless=False)
        cls.context = cls.browser.new_context(viewport={"width": 2560, "height": 1440}, ignore_https_errors=True)
        cls.page = cls.context.new_page()
        cls.config_read = ReadConfig()
        cls.url = cls.config_read.get_url()
        cls.username = cls.config_read.admin_username()
        cls.password = cls.config_read.admin_password()
        cls.add_quote = Add_Quote(cls.page)
        cls.page.goto(cls.url)
        cls.add_quote.typeUserName(cls.username)
        cls.add_quote.typePassword(cls.password)
        cls.add_quote.clicklogin()
        cls.add_quote.go_addquote()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.page.close()
        cls.context.close()
        cls.browser.close()
        cls.playwright.stop()

    def test_addquote_ui_001(self):
        '''Verify the url for Add Quotes page'''
        self.assertEqual('http://aabb/Quote/Create',self.add_quote.check_addquote_url)

    def test_addquote_ui_002(self):
        '''Verify the Save Quote button in Add Quotes page'''
        self.assertTrue(self.add_quote.check_savequote_btn)

    def test_addquote_ui_003(self):
        '''Verify each description of Proplsal Details in Add Quotes page'''
        self.assertEqual(('Proposal Number','Pricing Category','User','Account Type','Order Date',
                          'Quote Status','Account Customer','Supply Type'),self.add_quote.check_proposal_details)

    def test_addquote_ui_005(self):
        '''Verify each value in "Pricing Category" list, it should be 'Category 1','Category 2',
        'Category 3','Category 4','Company 1',"Wholesale"'''
        self.assertEqual(('Category 1\nCategory 2\nCategory 3\nCategory 4\nCompany 1\nWholesale\n'),
                         self.add_quote.check_pricing_cate_value)

    def test_addquote_ui_006(self):
        '''Verify the default value in "Pricing Category" list, it should be "Category 4"'''
        self.assertEqual(('Category 4'),self.add_quote.check_default_pricing)

    def test_addquote_ui_007(self):
        '''Verify the default value in "User" list, it should be current login user'''
        self.assertEqual(('Yi Sun'),self.add_quote.check_default_user)

    def test_addquote_ui_008(self):
        '''Verify each value in "Account Type" list, it should be 'Cash sale',"Account"'''
        self.assertEqual(('Cash sale\nAccount\n'),self.add_quote.check_accounttype_value)

    def test_addquote_ui_009(self):
        '''Verify the default value in "Account Type" list, it should be "Cash sale"'''
        self.assertEqual(('Cash sale'),self.add_quote.check_default_accounttype)

    def test_addquote_ui_010(self):
        '''Verify each value in "Quote Status" list, it should be 'Cash sale','Quote','Active',"Close"'''
        self.assertEqual(('Lead\nQuote\nActive\nClose\n'),self.add_quote.check_quotestatus_value)

    def test_addquote_ui_011(self):
        '''Verify the default quote status'''
        self.assertEqual(('Quote'),self.add_quote.check_default_quotestatus)


    def test_addquote_ui_012(self):
        '''Verify each value in "Supply Type" list'''
        self.assertEqual(('Please Select\nVIC – Install\nVIC – Pick Up\nVIC – Deliver\nNSW – Install\nNSW – Pick Up\n'
                          'NSW – Deliver\nACT – Deliver\nTAS – Deliver\nSA – Deliver\nQLD – Deliver\nQLD – Pick Up\n'
                          'QLD – Install\nWA – Install\nWA – Deliver\nWA – Pick Up\nSA – Install\nSA – Pick Up\n'),
                         self.add_quote.check_supplytype_value)

    def test_addquote_ui_013(self):
        '''Verify the default value in "Supply Type" list, it should be "Please Select"'''
        self.assertEqual('Please Select',self.add_quote.check_supplytype_default)

    def test_addquote_ui_014(self):
        '''Verify The "Account Customer" list should enable after select "Account" in "Account Type" list'''
        self.assertFalse(False,self.add_quote.check_changeto_Account)



if __name__ == '__main__':
    unittest.main(verbosity=2)