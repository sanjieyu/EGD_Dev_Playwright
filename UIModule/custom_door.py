# Author:Yi Sun(Tim) 2025-11-10

'''Custom Door Page'''

from playwright.sync_api import Page,expect
from UIModule.add_quote import Add_Quote

class Custom_Door(Add_Quote):

    def __init__(self,page:Page):
        super().__init__(page)
        self._init_locators_custom_door()

    def _init_locators_custom_door(self):
        self.add_door_menu = self.page.locator('#btnDoorSectionadd')
        self.add_custom_btn = self.page.locator('#add-door-custom')
        self.add_btn_loc = self.page.locator('#customAdd')
        self.close_customdoor_btn = self.page.locator('#customClose')
        self.door_main_page = self.page.locator('xpath=/html/body/div[3]/div[2]/div[3]/div/div/form/div')

        '''loc for each element for install details'''
        self.title_loc = self.page.locator('xpath=/html/body/div[3]/div[2]/div[3]/div/div/form/div/h1')
        self.unit_no_loc = self.page.locator('xpath=/html/body/div[3]/div[2]/div[3]/div/div/form/div/div[1]/div[2]/'
                                             'div[1]/label')
        self.unit_no_inputbox = self.page.locator('#CustomUnitNumber')
        self.packaging_type_loc = self.page.locator('xpath=/html/body/div[3]/div[2]/div[3]/div/div/form/div/div[1]/'
                                                    'div[2]/div[3]/label')
        self.packaging_type_select = self.page.locator( '#PackagingTypeCustom')

        self.install_type_loc = self.page.locator(
        'xpath=/html/body/div[3]/div[2]/div[3]/div/div/form/div/div[1]/div[4]/div[1]/fieldset/label')
        self.install_type_select = self.page.locator('#InstallType')
        self.design_loc = self.page.locator('xpath=/html/body/div[3]/div[2]/div[3]/div/div/form/div/div[1]/div[4]/'
                                            'div[2]/fieldset/label')
        self.design_select = self.page.locator('#CustomDesign')
        self.colour_category_loc = self.page.locator(
        'xpath=/html/body/div[3]/div[2]/div[3]/div/div/form/div/div[1]/div[4]/div[3]/fieldset/label')
        self.colour_category_select = self.page.locator('#CustomColourCategory')
        self.door_colour_loc = self.page.locator(
        'xpath=/html/body/div[3]/div[2]/div[3]/div/div/form/div/div[1]/div[4]/div[4]/fieldset/label')
        self.door_colour_select = self.page.locator('#CustomDoorColour')
        self.frame_colour_loc = self.page.locator(
        'xpath=/html/body/div[3]/div[2]/div[3]/div/div/form/div/div[1]/div[4]/div[5]/fieldset/label')
        self.frame_colour_select = self.page.locator('#CustomFrameColour')
        self.timber_profile_loc = self.page.locator(
         'xpath=/html/body/div[3]/div[2]/div[3]/div/div/form/div/div[1]/div[4]/div[6]/fieldset/label')
        self.timber_profile_select = self.page.locator('#ui-id-16')
        self.insert_material_loc = self.page.locator(
        'xpath=/html/body/div[3]/div[2]/div[3]/div/div/form/div/div[1]/div[4]/div[7]/fieldset/label')
        self.insert_material_select = self.page.locator('#CustomInsertMaterial')
        self.insert_location_loc = self.page.locator(
        'xpath=/html/body/div[3]/div[2]/div[3]/div/div/form/div/div[1]/div[4]/div[8]/fieldset/label')
        self.insert_location_select = self.page.locator( '#CustomInsertLocation')
        self.insert_type_loc = self.page.locator(
        'xpath=/html/body/div[3]/div[2]/div[3]/div/div/form/div/div[1]/div[4]/div[9]/fieldset/label')
        self.insert_type_select = self.page.locator('#CustomInsertType')
        self.insert_colour_loc = self.page.locator(
        'xpath=/html/body/div[3]/div[2]/div[3]/div/div/form/div/div[1]/div[4]/div[10]/fieldset/label')
        self.insert_colour_select = self.page.locator('#CustomInsertColour')
        self.insert_other_loc = self.page.locator(
        'xpath=/html/body/div[3]/div[2]/div[3]/div/div/form/div/div[1]/div[4]/div[11]/fieldset/label')
        self.insert_other_inputbox = self.page.locator('#CustomInsertOther')
        self.custom_colour_loc = self.page.locator(
        'xpath=/html/body/div[3]/div[2]/div[3]/div/div/form/div/div[1]/div[4]/div[12]/fieldset/label')
        self.custom_colour_inputbox = self.page.locator('#CustomCustomColour')

        '''loc for each element for SIZE details'''
        self.opensize_lh_loc = self.page.locator(
        'xpath=/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[4]/div[12]/fieldset/label')
        self.opensize_lh_select = self.page.locator('#CustomOpeningSizeLH')
        self.opensize_rh_loc = self.page.locator(
        'xpath=/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[4]/div[13]/fieldset/label')
        self.opensize_rh_select = self.page.locator('#CustomOpeningSizeRH')
        self.opensize_width_loc = self.page.locator(
        'xpath=/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[4]/div[14]/fieldset/label')
        self.opensize_width_select = self.page.locator('#CustomOpeningSizeWidth')
        self.sr_left_loc = self.page.locator(
        'xpath=/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[4]/div[15]/fieldset/label')
        self.sr_left_select = self.page.locator( '#CustomSRLeft')
        self.hr_loc = self.page.locator('xpath=/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[4]/div[16]/'
                                        'fieldset/label')
        self.hr_select = self.page.locator( '#CustomHR')
        self.sr_right_loc = self.page.locator(
        'xpath=/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[4]/div[17]/fieldset/label')
        self.sr_right_select = self.page.locator('#CustomSRRight')
        self.lhrk_loc = self.page.locator('xpath=/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[4]/div[18]/'
                                          'fieldset/label')
        self.lhrk_select = self.page.locator('#CustomLHRK')
        self.sms_bracket_loc = self.page.locator(
        'xpath=/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[4]/div[19]/fieldset/div/label')
        self.lsr_kit_loc = self.page.locator(
        'xpath=/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[4]/div[20]/fieldset/div/label')
        self.timber_packers_loc = self.page.locator(
        'xpath=/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[4]/div[21]/fieldset/label')
        self.timber_packers_select = self.page.locator( '#CustomTimberPackers')
        self.taper_loc = self.page.locator( 'xpath=/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[4]/'
                                            'div[22]/fieldset/label')
        self.taper_select = self.page.locator('#CustomTaper')
        self.additional_fabrication_loc = self.page.locator(
        'xpath=/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[4]/div[24]/fieldset/label')
        self.additional_fabrication_select = self.page.locator('#CustomHeavyAngle')
        self.additional_fabrication_required_loc = self.page.locator(
        'xpath=/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[4]/div[25]/fieldset/label')
        self.additional_fabrication_required_inputbox = self.page.locator( '#CustomHeavyAngleDetails')
        self.shop_drawings_loc = self.page.locator(
        'xpath=/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[4]/div[26]/fieldset/label')
        self.shop_drawings_select = self.page.locator('#CustomShopDrawings')
        self.lifting_equipment_loc = (
        'xpath=/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[4]/div[27]/fieldset/label')
        self.lifting_equipment_btn = self.page.locator(
        'xpath=/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[4]/div[27]/fieldset/span/div/button')

        '''loc for each element for Panels details'''
        self.panel_high_loc = self.page.locator(
        'xpath=/html/body/div[3]/div[2]/div[3]/div/div/form/div/div[1]/div[4]/div[23]/fieldset/label')
        self.panel_high_select_loc = self.page.locator( '#panels_high')
        self.panel_wide_loc = self.page.locator(
        'xpath=/html/body/div[3]/div[2]/div[3]/div/div/form/div/div[1]/div[4]/div[24]/fieldset/label')
        self.panel_wide_btn_loc = self.page.locator(
        'xpath=/html/body/div[3]/div[2]/div[3]/div/div/form/div/div[1]/div[4]/div[24]/fieldset/span/a')
        self.panel_wide_input_loc = self.page.locator('#panels_wide_part')

        '''loc for each element for checkboxes details'''
        self.induction_loop_loc = self.page.locator(
         'xpath=/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[4]/div[28]/fieldset/div[1]/div[1]/label')
        self.reverse_install_loc = self.page.locator(
        'xpath=/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[4]/div[28]/fieldset/div[2]/div[1]/label')
        self.fully_sloctted_loc = self.page.locator(
         'xpath=/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[4]/div[28]/fieldset/div[3]/div[1]/label')
        self.emergency_key_loc = self.page.locator(
         'xpath=/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[4]/div[28]/fieldset/div[1]/div[2]/label')
        self.reverse_colour_loc = self.page.locator(
        'xpath=/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[4]/div[28]/fieldset/div[2]/div[2]/label')
        self.battery_backup_loc = self.page.locator(
        'xpath=/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[4]/div[28]/fieldset/div[3]/div[2]/label')
        self.eco_wifi_loc = self.page.locator(
         'xpath=/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[4]/div[28]/fieldset/div[1]/div[3]/label')

        '''loc for Opener details'''
        self.opener_loc = self.page.locator('xpath=/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[4]/'
                                            'div[30]/fieldset/label')
        self.opener_select = self.page.locator( '#CustomMotors')
        self.handsets_loc = self.page.locator(
         'xpath=/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[4]/div[31]/fieldset/label')
        self.handsets_select = self.page.locator( '#CustomNoOfHandsets')
        self.wall_btn_loc = self.page.locator(
        'xpath=/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[4]/div[32]/fieldset/label')
        self.wall_btn_select = self.page.locator( '#CustomWallButton')
        self.opener_detail_loc = self.page.locator(
        'xpath=/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[4]/div[33]/fieldset/label')
        self.opener_detail_box = self.page.locator('#CustomMotorsOther')
        self.digital_keypad_loc = (
        'xpath=/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[4]/div[34]/fieldset/label')
        self.digital_keypad_select = self.page.locator('#CustomDigitalKeypad')
        self.internal_pushbtn_loc = self.page.locator(
        'xpath=/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[4]/div[35]/fieldset/label')
        self.internal_pushbtn_select = self.page.locator( '#CustomInternalPushButton')
        self.pe_beam_loc = self.page.locator(
        'xpath=/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[4]/div[36]/fieldset/label')
        self.pe_beam_select = self.page.locator('#PEBeamCustom')
        self.pe_beam_sets_loc = self.page.locator(
         'xpath=/html/body/div[3]/div[2]/div[2]/div/div/div/form/div[1]/div[4]/div[37]/fieldset/label')
        self.pe_beam_sets_select = self.page.locator('#PEBeamSetsCustom')


    def go_addcustomdoor(self):
        '''Open the Add Custom Door from Quote Page'''
        self.add_door_menu.click()
        self.add_custom_btn.click()
        self.page.wait_for_timeout(2000)
        all_pages = self.page.context.pages
        new_page = all_pages[-1]
        new_page.bring_to_front()
        self.page = new_page

    @property
    def check_customdoor_page(self):
        '''check the main elements in the page'''
        standarddoor_title = self.title_loc.inner_text()
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        print(standarddoor_title)
        return standarddoor_title

    @property
    def check_install_details(self):
        '''check each element for install details'''
        install_type = self.install_type_loc.inner_text()
        design = self.design_loc.inner_text()
        colour_category = self.colour_category_loc.inner_text()
        door_colour = self.door_colour_loc.inner_text()
        frame_colour = self.frame_colour_loc.inner_text()
        timber_profile = self.timber_profile_loc.inner_text()
        insert_material = self.insert_material_loc.inner_text()
        insert_location = self.insert_location_loc.inner_text()
        insert_type = self.insert_type_loc.inner_text()
        insert_colour = self.insert_colour_loc.inner_text()
        insert_other = self.insert_other_loc.inner_text()
        custom_colour = self.custom_colour_loc.inner_text()
        print(install_type, design, colour_category, door_colour, frame_colour, timber_profile, insert_material,
              insert_location, insert_type, insert_colour, insert_other, custom_colour)
        return (install_type, design, colour_category, door_colour, frame_colour, timber_profile, insert_material,
                insert_location, insert_type, insert_colour, insert_other, custom_colour)

    @property
    def check_door_colour_custom(self):
        '''check the Door Colour dropdown for Custom Colour Category'''
        # global colour_category
        custom_colour = self.colour_category_select.select_option(label='Custom')
        door_colour_list = self.door_colour_select
        if door_colour_list.is_enabled():
            print('Enabled')
            return True
        else:
            print("Disabled")
            return False

    @property
    def check_door_colour_oilcolour(self):
        '''check the Door Colour dropdown for OilColour Colour Category'''
        custom_colour = self.colour_category_select.select_option(label='OilColour')
        self.door_colour_select.click()
        door_colour_list1 = self.door_colour_select.text_content()
        print(door_colour_list1)
        return door_colour_list1

    @property
    def check_door_colour_sealedcolour(self):
        '''check the Door Colour dropdown for SealedColour Colour Category'''
        custom_colour = self.colour_category_select.select_option(label='SealedColour')
        door_colour_list4 = self.door_colour_select.text_content()
        print(door_colour_list4)
        return door_colour_list4

    @property
    def check_insert_material(self):
        '''check the Insert Material dropdown list'''
        self.insert_material_select.click()
        insert_material_list = self.insert_material_select.text_content()
        print(insert_material_list)
        return insert_material_list

    @property
    def check_insert_type_cat1(self):
        '''check the Insert Type dropdown if set "ACPS Cat1" in Insert Material category'''
        material_value = self.insert_material_select.select_option(label='ACPS Upgrade - Cat 1')
        self.insert_type_select.click()
        insert_type_list1 = self.insert_type_select.evaluate("""
                element => {
                    const options = Array.from(element.options);
                    return options.map(option => option.textContent).join('\\n');
                }
            """)
        print(insert_type_list1)
        return insert_type_list1



if __name__ == "__main__":
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page(viewport={"width": 2560, "height": 1440})
        # page = browser.new_page()
        page.goto("http://  ")
        login = Custom_Door(page)
        login.typeUserName('aabb')
        login.typePassword('aabb')
        login.clicklogin()
        page.wait_for_timeout(2000)
        login.go_addquote()
        login.go_addcustomdoor()
        # login.add_custom_detail()
        # login.check_customdoor_page
        # login.check_install_details
        # login.check_door_colour_custom
        # login.check_door_colour_oilcolour
        # login.check_door_colour_sealedcolour
        # login.check_insert_material
        # login.check_insert_type_cat1


