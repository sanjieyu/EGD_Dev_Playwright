# Author:Yi Sun(Tim) 2025-11-12

'''Add Standard Door Details Page'''

from playwright.sync_api import Page,expect
from UIModule.add_quote import Add_Quote

class Standard_Door(Add_Quote):

    def __init__(self,page:Page):
        super().__init__(page)
        self._init_locators_standard_door()

    def _init_locators_standard_door(self):
        self.standard_door_menu = self.page.locator('#add-door-btn')
        self.add_standarddoor_btn = self.page.locator('#btnDoorAdd')
        self.close_standarddoor_btn = self.page.locator('#btnDoorClose')
        self.door_main_page = self.page.locator('xpath=//*[@id="main"]/div/span')

        '''loc for each element for install details'''
        self.title_loc = self.page.locator("[name='QuoteTitle']")
        self.storage_bay_no_loc = self.page.locator("[name='StorageBay']")
        self.unit_no_loc = self.page.locator("[name='UnitNum']")
        self.unit_no_inputbox = self.page.locator('#UnitNumber')
        self.packaging_type_loc = self.page.locator("[name='PackagingType']")
        self.packaging_type_select = self.page.locator('#PackagingType')
        self.install_type_loc = self.page.locator("[name='InstallTypeStandardEdit']")
        self.install_type_select = self.page.locator('#InstallTypeStandard')
        self.door_type_loc = self.page.locator("[name='DoorTypeEdit']")
        self.door_type_select = self.page.locator('#DoorType')
        self.design_loc = self.page.locator("[name='DesignEdit']")
        self.design_select = self.page.locator( '#Door_Design')
        self.colour_category_loc = self.page.locator("[name='CategoryEdit']")
        self.colour_category_select = self.page.locator('#Door_Color_Category')
        self.door_colour_loc = self.page.locator("[name='ColorEdit']")
        self.door_colour_select = self.page.locator('#DoorColor')
        self.door_finish_loc = self.page.locator(("[name='FinishEdit']")
        self.door_finish_select = self.page.locator('#DoorFinish')
        self.custom_colour_loc = self.page.locator("[name='CustomColorEdit']")
        self.custom_colour_inputbox = self.page.locator('#Door_Custom_Color')
        self.tech_measure_loc = self.page.locator("[name='TechEdit']")
        self.measure_require_loc = self.page.locator("[name='MeasureEdit']")

        '''loc for each element for SIZE details'''
        self.opensize_lh_loc = self.page.locator("[name='OpeningSizeLHEdit']")
        self.opensize_lh_select = self.page.locator('#OpeningSizeLH')
        self.opensize_rh_loc = self.page.locator("[name='OpeningSizeRHEdit']")
        self.opensize_rh_select = self.page.locator('#OpeningSizeRH')
        self.opensize_width_loc = self.page.locator("[name='OpeningSizeWidthEdit']")
        self.opensize_width_select = self.page.locator('#OpeningSizeWidth')
        self.sr_left_loc = self.page.locator("[name='SRLeftEdit']")
        self.sr_left_select = self.page.locator('#SR_left')
        self.hr_loc = self.page.locator("[name='HREdit']")
        self.hr_select = self.page.locator('#HR')
        self.sr_right_loc = self.page.locator("[name='SRRightEdit']")
        self.sr_right_select = self.page.locator('#SR_right')
        self.lhrk_loc = self.page.locator("[name='LHRKEdit']")
        self.lhrk_select = self.page.locator('#LHRK')
        self.sms_bracket_loc = self.page.locator("[name='SMSEdit']")
        self.lsr_kit_loc = self.page.locator("[name='LsrEdit']")
        self.timber_packers_loc = self.page.locator("[name='TimberPackersEdit']")
        self.timber_packers_select = self.page.locator('#TimberPackers')
        self.taper_loc = self.page.locator("[name='TapeEdit']")
        self.taper_select = self.page.locator('#Taper')
        self.additional_fabrication_loc = self.page.locator("[name='HeavyAngleEdit']")
        self.additional_fabrication_required_loc = self.page.locator("[name='HeavyAngleDetailsEdit']")
        self.additional_fabrication_required_inputbox = self.page.locator('#HeavyAngleDetails')
        self.shop_drawings_loc = self.page.locator("[name='ShopDrawingsEdit']")
        self.shop_drawings_select = self.page.locator('#ShopDrawings')
        self.lifting_equipment_loc = self.page.locator("[name='LiftEdit']")
        self.lifting_equipment_btn = self.page.locator("#btnLift")

        '''loc for each element for checkboxes details'''
        self.induction_loop_loc = self.page.locator('xpath=//*[@id="induction"]/div/div[1]')
        self.induction_loop_box_loc = self.page.locator( '#IsInductionLoopStandard')
        self.fully_sloctted_loc = self.page.locator('xpath=//*[@id="sloctted"]/div/div[1]/div[2]/span')
        self.fully_slotted_box_loc = self.page.locator( '#IsFullySlottedStandard')
        self.emergency_key_loc = self.page.locator('xpath=//*[@id="emergency"]/div/div[2]/span')
        self.emergency_key_box_loc = self.page.locator( '#PriceEmergencyKeyRelease')
        self.reverse_colour_loc = self.page.locator('xpath=//*[@id="reversecolour"]/div/div[2]/span')
        self.reverse_colour_box_loc = self.page.locator('#IsReverseColourStandard')
        self.battery_backup_loc = self.page.locator('xpath=//*[@id="battery"]/div/div[3]/span')
        self.attery_backup_box_loc = self.page.locator( '#IsBatteryBackupStandard')
        self.eco_wifi_loc = self.page.locator( 'xpath=//*[@id="ecowifi"]/div/div[2]/span')
        self.eco_wifi_box_loc = self.page.locator('#IsWiFi')

        '''loc for Opener details'''
        self.opener_loc = self.page.locator( 'xpath=//*[@id="opener"]/div/div[1]/div[2]/span)
        self.opener_select = self.page.locator( '#Motors')
        self.handsets_loc = self.page.locator( 'xpath=//*[@id="handsets"]/div/div[1]/div[2]/span')
        self.handsets_select = self.page.locator('#Handset')
        self.wall_btn_loc = self.page.locator( 'xpath=//*[@id="wallbtn"]/div/div[1]/span')
        self.wall_btn_select = self.page.locator( '#Door_Wall_Button')
        self.opener_detail_loc = self.page.locator( 'xpath=//*[@id="motorsother"]/div/div[2]/span')
        self.opener_detail_box = self.page.locator( '#MotorsOther')
        self.digital_keypad_loc = self.page.locator('xpath=//*[@id="keypad"]/div/div[1]')
        self.digital_keypad_select = self.page.locator('#DigitalKeypad')
        self.internal_pushbtn_loc = self.page.locator('xpath=//*[@id="pushbtn"]/div/div[2]')
        self.internal_pushbtn_select = self.page.locator( '#InternalPushButton')
        self.pe_beam_loc = self.page.locator( 'xpath=//*[@id="pe_beam"]/div/div[2]/span')
        self.pe_beam_select = self.page.locator('#PEBeamGeneral')
        self.pe_beam_sets_loc = self.page.locator( 'xpath=//*[@id="beam_sets"]/div/div[2]/span')
        self.pe_beam_sets_select = self.page.locator( '#PEBeamSetsGeneral')
        self.keys_loc = self.page.locator( 'xpath=//*[@id="keys"]/div/div[2]/span')
        self.keys_select = self.page.locator('#Keys')

        '''loc for other elements details '''
        self.weight_added_loc = self.page.locator("label[for='WeightBeingAdded']")
        self.weight_added_select = ('#WeightAddedStandard')
        self.seals_loc = self.page.locator("label[for='CustomSeals']")
        self.seals_select = self.page.locator('#Seals')
        self.dealer_seals2500_loc = self.page.locator("label[for='CustomSeals2500']")
        self.dealer_seals3000_loc = self.page.locator("label[for='CustomSeals3000']")
        self.hang_door_loc = self.page.locator("label[for='CustomHangDoorFrom']")
        self.hang_door_select = self.page.locator('#hang_door_from_standard_part')
        self.lintel_type_loc = self.page.locator("label[for='CustomLintelType']")
        self.lintel_type_select = self.page.locator('#LintelType')
        self.fixing_type_loc = self.page.locator("label[for='CustomFixingType']")
        self.fixing_type_select = self.page.locator('#fixing_type_standard_part')
        self.ibeam_noggins_loc = self.page.locator("label[for='CustomIBeamNoggins']")
        self.ibeam_noggins_select = self.page.locator('#noggins_standard_part')
        self.remove_dispose_loc = self.page.locator("label[for='RemoveDispose']")
        self.remove_dispose_select = self.page.locator('#RemoveAndDispose')
        self.job_status_loc = self.page.locator("label[for='JobStatus']")
        self.job_status_select = self.page.locator( '#JobStatusId')
        self.expected_deliverydate_loc = self.page.locator("label[for='DeliveryDate']")
        self.expected_deliverydate_box = self.page.locator( '#ExpectedDeliveryDate')
        self.cut_date_loc = self.page.locator("label[for='CutDate']")
        self.cut_date_box = self.page.locator( '#CutDate')
        self.paint_date_loc = self.page.locator("label[for='PaintDate']")
        self.qc_date_loc = self.page.locator("label[for='QcDate']")
        self.qc_date_box = self.page.locator( '#QCDate')
        self.other_date_loc = self.page.locator("label[for='OtherDate']")
        self.other_date_box = self.page.locator('#OtherDate')

        '''loc for additional infomation details '''
        self.additional_info_loc = self.page.locator("label[for='AdditionalInfo']")
        self.additional_info_box = self.page.locator('#AdditionalInfo')
        self.production_notes_loc = self.page.locator("label[for='ProductionNotes']")
        self.production_notes_box = self.page.locator('#ProductionNotes')

    def go_addstandarddoor(self):
        '''Open the Add Standard Door from Quote Page'''
        self.supply_type_select.select_option(label='WA – Install')  # set the supply type to WA
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        self.add_door_btn.click()
        self.standard_door_menu.click()
        self.page.wait_for_timeout(4000)
        all_pages = self.page.context.pages
        new_page = all_pages[-1]
        new_page.bring_to_front()
        self.page = new_page

    @property
    def check_door_page(self):
        '''check the main elements in the page'''
        standarddoor_title=self.title_loc.inner_text()
        self.add_standarddoor_btn.scroll_into_view_if_needed()
        add_button = self.add_standarddoor_btn.inner_text()
        print(standarddoor_title, add_button)
        return standarddoor_title, add_button

    @property
    def check_install_details(self):
        '''check each element for install details'''
        install_type = self.install_type_loc.inner_text()
        door_type = self.door_type_loc.inner_text()
        design = self.design_loc.inner_text()
        colour_category = self.colour_category_loc.inner_text()
        door_colour = self.door_colour_loc.inner_text()
        door_finish = self.door_finish_loc.inner_text()
        custom_colour = self.custom_colour_loc.inner_text()
        tech_measure = self.tech_measure_loc.inner_text()
        measure_require = self.measure_require_loc.inner_text()
        print(install_type, door_type, design, colour_category, door_colour, door_finish, custom_colour, tech_measure,
              measure_require)
        return (install_type, door_type, design, colour_category, door_colour, door_finish, custom_colour, tech_measure,
                measure_require)

    @property
    def check_install_type(self):
        '''check the install type dropdown'''
        self.install_type_select.click()
        install_type_list = self.install_type_select.text_content()
        print(install_type_list)
        return install_type_list

    @property
    def check_door_type(self):
        '''check the Door type dropdown'''
        self.door_type_select.click()
        door_type_list = self.door_type_select.text_content()
        print(door_type_list)
        return door_type_list

    @property
    def check_colour_category(self):
        '''check the Colour Category dropdown'''
        self.colour_category_select.click()
        colour_category_list =self.colour_category_select.evaluate("""
                element => {
                    const options = Array.from(element.options);
                    return options.map(option => option.textContent).join('\\n');
                }
            """)
        print(colour_category_list)
        return colour_category_list

    @property
    def check_design_panel(self):
        '''check the Design dropdown for Panel Lift-Safe Door'''
        self.door_type_select.select_option(label='Panel Lift-Safe')
        self.design_select.click()
        design_list = self.design_select.evaluate("""
                element => {
                    const options = Array.from(element.options);
                    return options.map(option => option.textContent).join('\\n');
                }
            """)
        print(design_list)
        return design_list

    @property
    def check_design_insulated(self):
        '''check the Design dropdown for Insulated Sectional Door'''
        self.door_type_select.select_option(label='Insulated Sectional')
        self.design_select.click()
        design_list = self.design_select.evaluate("""
                element => {
                    const options = Array.from(element.options);
                    return options.map(option => option.textContent).join('\\n');
                }
            """)
        print(design_list)
        return design_list


if __name__ == "__main__":
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page(viewport={"width": 2048, "height": 1152})
        # page = browser.new_page()
        page.goto("http:// ")
        login = Standard_Door(page)
        login.typeUserName('aabb')
        login.typePassword('aabb')
        login.clicklogin()
        page.wait_for_timeout(2000)
        login.go_addquote()
        login.go_addstandarddoor()
        # login.check_door_page
        # login.check_install_details
        # login.check_install_type
        # login.check_door_type
        # login.check_colour_category
        login.check_design_panel



