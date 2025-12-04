# Author:Yi Sun(Tim) 2025-11-19

'''Test Search Quote Page'''

import unittest
from playwright.sync_api import sync_playwright,expect
from UIModule.search_quote import Search_Quote
from CommomModule.read_config import *

class TestSearchQuote(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.firefox.launch(headless=False)
        cls.page = cls.browser.new_page(viewport={"width": 2560, "height": 1440})
        cls.config_read = ReadConfig()
        cls.url = cls.config_read.get_url()
        cls.username = cls.config_read.admin_username()
        cls.password = cls.config_read.admin_password()
        cls.search_quote = Search_Quote(cls.page)
        cls.page.goto(cls.url)
        cls.search_quote.typeUserName(cls.username)
        cls.search_quote.typePassword(cls.password)
        cls.search_quote.clicklogin()
        cls.search_quote.go_searchquotes()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.page.close()
        cls.browser.close()
        cls.playwright.stop()

    def test_searchquotes_ui_001(self):
        '''Verify the url for Search Quotes page'''
        self.assertEqual('http://aabb/Quote/List',self.search_quote.check_searchurl)

    def test_searchquotes_ui_002(self):
        '''Verify the title for Search Quotes page'''
        self.assertEqual('Search Quotes',self.search_quote.check_title)
    def test_searchquotes_ui_003(self):
        '''Verify the default section should be "Quotes" in Search Quotes page'''
        self.assertTrue(self.search_quote.check_defaulsection)

    def test_searchquotes_ui_004(self):
        '''Verify the default elements in Search Quotes page'''
        self.assertEqual(('Quotes','Doors','Search Results'),self.search_quote.check_defaultelements)

    def test_searchquotes_ui_005(self):
        '''Verify each section of Quotes filter table in Search Quotes page'''
        self.assertEqual(('Date Range','Client Details','Quote Information'),self.search_quote.check_section_quotes)

    def test_searchquotes_ui_006(self):
        '''Verify each filter in "Date Range" in Quotes filter table'''
        self.assertEqual(('Filter Date','User','Quote Status'),self.search_quote.check_date_range)

    def test_searchquotes_ui_007(self):
        '''Verify each filter in "Client Details" in Quotes filter table'''
        self.assertEqual(('Client Name','Contact Number','Suburb','Postcode'),self.search_quote.check_client_details)

    def test_searchquotes_ui_008(self):
        '''Verify each filter in "Quote Information" in Quotes filter table'''
        self.assertEqual(('Proposal No','Door Design','Colour Category','Door Colour','Site Address'),
                         self.search_quote.check_quote_info)

    def test_searchquotes_ui_009(self):
        '''Verify the default user name in "User" filter in Quotes filter table, should be the current login user'''
        self.assertEqual(('Yi Sun'),self.search_quote.check_default_user)

    def test_searchquotes_ui_010(self):
        '''Verify the search by client name function, should find the correct proposal No. for this client'''
        self.assertEqual(('208849'),self.search_quote.search_client_name)

    def test_searchquotes_ui_011(self):
        '''Verify the search by Proposal ID function, should find the correct proposal No. for this client'''
        self.assertEqual(('210088'),self.search_quote.search_proposal_id)
    def test_searchquotes_ui_012(self):
        '''Verify the search by Contact Number function, should find the correct proposal No. for this client'''
        self.assertEqual(('210088'),self.search_quote.search_contact_num)

    def test_searchquotes_ui_013(self):
        '''Verify the search by Suburb function, should find the correct proposal No. for this client'''
        self.assertEqual(('210088'),self.search_quote.search_suburb)

    def test_searchquotes_ui_014(self):
        '''Verify the search by Postcode function, should find the correct proposal No. for this client'''
        self.assertEqual(('210088'),self.search_quote.search_postcode)

    def test_searchquotes_ui_015(self):
        '''Verify the search by Door Design function, should find the correct proposal No. for this client'''
        self.assertEqual(('204532'),self.search_door_design)

    def test_searchquotes_ui_016(self):
        '''Verify the search by Door Colour function, should find the correct proposal No. for this client'''
        self.assertEqual(('210392'),self.search_quote.search_door_colour)

    def test_searchquotes_ui_017(self):
        '''Verify the search by Colour Category function, should find the correct proposal No. for this client'''
        self.assertEqual(('204531'),self.search_door_category)

if __name__ == '__main__':
    unittest.main(verbosity=2)
