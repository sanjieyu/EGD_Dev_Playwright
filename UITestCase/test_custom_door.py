# Author:Yi Sun(Tim) 2025-11-10

'''Test Custom Door Page'''

import unittest
from playwright.sync_api import sync_playwright,expect
from UIModule.custom_door import Custom_Door
from CommomModule.read_config import *

class TestCustomDoor(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.firefox.launch(headless=False)
        cls.page = cls.browser.new_page(viewport={"width": 2560, "height": 1440})
        cls.config_read = ReadConfig()
        cls.url = cls.config_read.get_url()
        cls.username = cls.config_read.admin_username()
        cls.password = cls.config_read.admin_password()
        cls.custom_door = Custom_Door(cls.page)
        cls.page.goto(cls.url)
        cls.custom_door.typeUserName(cls.username)
        cls.custom_door.typePassword(cls.password)
        cls.custom_door.clicklogin()
        cls.custom_door.go_addquote()
        cls.custom_door.go_addcustomdoor()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.page.close()
        cls.browser.close()
        cls.playwright.stop()

    def test_add_customdoor_ui_001(self):
        '''Verify the main elements in the page '''
        self.assertEqual(('Custom Door Details'),self.custom_door.check_customdoor_page)

    def test_add_customdoor_ui_002(self):
        '''Verify each element for install details'''
        self.assertEqual(('Install Type','Design','Colour Category','Door Colour','Frame Colour','Timber Profile',
                          'Insert Material','Insert Location','Insert Type','Insert Colour','Insert Other','Custom Colour'),
                         self.custom_door.check_install_details)

    def test_add_customdoor_ui_006(self):
            '''Verify the Door Colour dropdown list should be diabled if select "Custom" in Colour Category '''
            self.assertFalse(self.custom_door.check_door_colour_custom)

    def test_add_customdoor_ui_007(self):
        '''Verify the Door Colour dropdown if select "OliColour" in Colour Category '''
        self.assertEqual(('Please SelectBlack AshClearCustomSela BrownTBA'), self.custom_door.check_door_colour_oilcolour)


    def test_add_customdoor_ui_010(self):
            '''Verify the Door Colour dropdown if select "SealedColour" in Colour Category '''
            self.assertEqual(('Please SelectClearCustomDark oakEbonyHemlockLight oakRosewoodTBAWalnut'),
                             self.custom_door.check_door_colour_sealedcolour)

    def test_add_customdoor_ui_013(self):
            '''Verify the Insert Material dropdown list '''
            self.assertEqual(('Please Select\nACPS Upgrade - Cat 1\nACPS Upgrade - Cat 2\nAcrylic\nAluminium\nExterier Ply\n'
                              'Glass\nOther\nPolycarbonate\nStandard ACPS\nSupplied By Client\nTBA\n'),
                             self.custom_door.check_insert_material)

    def test_add_customdoor_ui_016(self):
            '''Verify the Insert Type dropdown if select "ACPS Cat1" in Insert Material category'''
            self.assertEqual(('Please Select\nAlutile\nOther\nUltrabond\nVitrabond'),
                             self.custom_door.check_insert_type_cat1)

if __name__ == '__main__':
    unittest.main(verbosity=2)
