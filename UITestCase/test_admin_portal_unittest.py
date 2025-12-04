# Author:Yi Sun(Tim) 2025-10-28

'''Test Admin Portal Page by Unittest'''

from playwright.sync_api import sync_playwright,expect
import unittest
from UIModule.admin_portal import Admin_Page
from CommomModule.read_config import *

class TestAdminPortal(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """setup"""
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.firefox.launch(headless=False)
        cls.page = cls.browser.new_page(viewport={"width": 2560, "height": 1600})
        cls. config_read = ReadConfig()
        cls. url = cls.config_read.get_url()
        cls. admin_username = cls.config_read.admin_username()
        cls.admin_password = cls.config_read.admin_password()
        cls.admin_page = Admin_Page(cls.page)
        cls.page.goto(cls.url)
        cls.admin_page.typeUserName(cls.admin_username)
        cls.admin_page.typePassword(cls.admin_password)
        cls.admin_page.clicklogin()

    # def setUp(self) -> None:
    #     """setup """
    #     self.page = self.browser.new_page(viewport={"width": 2560, "height": 1600})
    #     self.admin_page = Admin_Page(self.page)
    #     self.page.goto("http://egd2.sighte.com/")
    #     self.admin_page.typeUserName('ysun@ecogaragedoors.com.au')
    #     self.admin_page.typePassword('Tims@123')
    #     self.admin_page.clicklogin()

    # def tearDown(self) -> None:
    #     """teardown""
    #     self.page.close()

    @classmethod
    def tearDownClass(cls) -> None:
        """teardown """
        cls.page.close()
        cls.browser.close()
        cls.playwright.stop()

    def test_adminportal_ui_001(self):
        '''Verify the url of Admin login Page'''
        self.assertEqual("http://egd2.sighte.com/",self.admin_page.getURL)

    def test_adminportal_ui_002(self):
        self.assertEqual(('ADD','LIST','ACCOUNT'),self.admin_page.check_defaultmenu)

    def test_check_find_quote(self):
        self.assertEqual(True,self.admin_page.check_findquote)

    def test_adminportal_ui_003(self):
        self.assertTrue(self.admin_page.check_findclient)

    def test_adminportal_ui_004(self):
        self.assertEqual(('© 2025 - EcoGarageDoors','Terms and Policies'),self.admin_page.check_copyright)


if __name__ == "__main__":
    unittest.main(verbosity=2)