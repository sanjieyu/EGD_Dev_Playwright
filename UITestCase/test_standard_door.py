# Author:Yi Sun(Tim) 2025-11-13

'''Test Standard Door Page'''

import unittest
from playwright.sync_api import sync_playwright,expect
from UIModule.add_standard import Standard_Door
from CommomModule.read_config import *

class TestStandardDoor(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.firefox.launch(headless=False)
        cls.page = cls.browser.new_page(viewport={"width": 2560, "height": 1440})
        cls.config_read = ReadConfig()
        cls.url = cls.config_read.get_url()
        cls.username = cls.config_read.admin_username()
        cls.password = cls.config_read.admin_password()
        cls.standard_door = Standard_Door(cls.page)
        cls.page.goto(cls.url)
        cls.standard_door.typeUserName(cls.username)
        cls.standard_door.typePassword(cls.password)
        cls.standard_door.clicklogin()
        cls.standard_door.go_addquote()
        cls.standard_door.go_addstandarddoor()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.page.close()
        cls.browser.close()
        cls.playwright.stop()

    def test_add_standarddoor_ui_001(self):
        '''Verify the main elements in the page, should including correct title, Add button and Close button '''
        self.assertEqual(('Standard Door Details', 'Add'), self.standard_door.check_door_page)

    def test_add_standarddoor_ui_002(self):
        '''Verify each element for install details'''
        self.assertEqual(('Install Type', 'Door Type', 'Design', 'Colour Category', 'Door Colour', 'Door Finish',
                          'Custom Colour', 'Technician Measure', 'Measure Required'), self.standard_door.check_install_details)

    @unittest.skip
    def test_add_standarddoor_ui_003(self):
        '''Verify the Install Type dropdown list '''
        self.assertEqual(('Please Select\nCommercial Cat 1\nCommercial Cat 2\nCommercial STD\nFull Panel Replacement\n'
                          'Panel Replacement\nResidential\n'), self.standard_door.check_install_type)
    @unittest.skip
    def test_add_standarddoor_ui_004(self):
        '''Verify the Door Type dropdown list'''
        self.assertEqual(('Please Select\nExoRoll\nInsulated Sectional\nOptiLift\nOptiRoll\nPanel Lift-Safe\n'),
                         self.standard_door.check_door_type)

    def test_add_standarddoor_ui_005(self):
            '''Verify the Colour Category dropdown list'''
            self.assertEqual(('Please Select\nColorBond\nColourbond Non Std\nCustom\nFlexigraphic\nFlexographic\nMetalFx\n'
                              'OilColor\nPainted Finish\nPortabella\nPowderCoatStandard\nPowderCoatUpgrade\nSealedColor\n'
                              'Timber Essence\nTimberFX'),self.standard_door.check_colour_category)

    def test_add_standarddoor_ui_006(self):
            '''Verify the Design dropdown for Panel Lift-Safe Door '''
            self.assertIn(('Slimline\nClassic panel\nLincoln panel\nUltraline\nWideline'),self.standard_door.check_design_panel)

    def test_add_standarddoor_ui_007(self):
        '''Verify the Design dropdown for Insulated Sectional Door'''
        self.assertIn(('Ribline\nFineline\nFlatline\nStanford'), self.standard_door.check_design_insulated)


if __name__ == '__main__':
    unittest.main(verbosity=2)
