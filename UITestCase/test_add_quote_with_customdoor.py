# Author:Yi Sun(Tim) 2025-11-27

'''Test Add a Quote with a Custom door function'''

import unittest
from playwright.sync_api import sync_playwright
from UIModule.add_quote_with_custom_door import Add_Quote_With_CustomDoor
from CommomModule.read_config import *

class TestAddQuoteWithCustomDoor(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.playwright = sync_playwright().start()
        cls. browser = cls.playwright.firefox.launch(headless=False)
        cls.context = cls.browser.new_context(viewport={"width": 2560, "height": 1440}, ignore_https_errors=True)
        cls.page = cls.context.new_page()
        cls.config_read = ReadConfig()
        cls.url = cls.config_read.get_url()
        cls.username = cls.config_read.admin_username()
        cls.password = cls.config_read.admin_password()
        cls.addquote_with_custom_door = Add_Quote_With_CustomDoor(cls.page)
        cls.page.goto(cls.url)
        cls.addquote_with_custom_door.typeUserName(cls.username)
        cls.addquote_with_custom_door.typePassword(cls.password)
        cls.addquote_with_custom_door.clicklogin()
        cls.addquote_with_custom_door.add_custom_door_fun()
        cls.addquote_with_custom_door.get_proposal_number
        cls.addquote_with_custom_door.search_new_quote()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.page.close()
        cls.context.close()
        cls.browser.close()
        cls.playwright.stop()

    def test_addquote_withcustomdoor_fun_001(self):
        '''Verify  Add a Quote with a Custom door function'''
        self.assertEqual(('Door 1(A1)','Quote'),self.addquote_with_custom_door.verify_new_quote)

if __name__ == '__main__':
    unittest.main(verbosity=2)
