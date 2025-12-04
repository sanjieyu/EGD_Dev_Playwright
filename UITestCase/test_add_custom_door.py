# Author:Yi Sun(Tim) 2025-11-11

'''Test Add Custom Door Func'''

import unittest
from playwright.sync_api import sync_playwright,expect
from UIModule.add_custom_door import Add_Custom_Door
from CommomModule.read_config import *

class TestAddCustomDoor(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.firefox.launch(headless=False)
        cls.page = cls.browser.new_page(viewport={"width": 2048, "height": 1152})
        cls.config_read = ReadConfig()
        cls.url = cls.config_read.get_url()
        cls.username = cls.config_read.admin_username()
        cls.password = cls.config_read.admin_password()
        cls.add_custom_door = Add_Custom_Door(cls.page)
        cls.page.goto(cls.url)
        cls.add_custom_door.typeUserName(cls.username)
        cls.add_custom_door.typePassword(cls.password)
        cls.add_custom_door.clicklogin()
        cls.add_custom_door.go_addquote()
        cls.add_custom_door.go_addcustomdoor()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.page.close()
        cls.browser.close()
        cls.playwright.stop()

    def test_add_customdoor_fun_001(self):
            '''Verify the input validation when add a new door'''
            self.assertIn(('Errors\nFor current Headroom height, pelmet is required\nPanels Wide should be selected\n'
                           'Packaging Type must be selected.\nIf SR (left) is less than 89mm, LH Jamb should be minimum 90mm.\n'
                           'If SR (right) is less than 89mm, RH Jamb should be minimum 90mm.\nMotors field is required'),
                          self.add_custom_door.validation_input)

    def test_add_customdoor_fun_002(self):
            '''Verify the add door function'''
            self.add_custom_door.add_custom_detail()
            self.assertEqual(('Custom Door, Residential, OilColour (10 x 60)'), self.add_custom_door.new_added_custom_door)

    def test_add_customdoor_fun_003(self):
            '''Verify the duplicate button for the new added door'''
            self.assertTrue(self.add_custom_door.duplicate_btn)

    def test_add_customdoor_fun_004(self):
            '''Verify the delete button for the new added door'''
            self.assertTrue(self.add_custom_door.delete_btn)

if __name__ == '__main__':
        unittest.main(verbosity=2)

