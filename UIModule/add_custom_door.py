# Author:Yi Sun(Tim) 2025-10-16

'''Add a Custom Door'''

from playwright.sync_api import Page,expect
from UIModule.custom_door import Custom_Door

class Add_Custom_Door(Custom_Door):

    def __init__(self,page):
        super().__init__(page)
        self._init_locators_add_custom_door()

    def _init_locators_add_custom_door(self):
        self.new_door_page_loc = self.page.locator('#customDoorForm')
        self.new_door_title = self.page.locator('#btnShowDoor')
        self.new_door_duplicate = self.page.locator('xpath=/html/body/div[3]/div[2]/div[1]/div/fieldset/div/div/'
                                                    'div[1]/div/div/div/div[3]/a[1]')
        self.new_door_delete = self.page.locator('xpath=/html/body/div[3]/div[2]/div[1]/div/fieldset/div/div/div[1]/'
                                                 'div/div/div/div[3]/a[2]')

        '''loc for validation'''
        self.validation_msgbox_loc = self.page.locator('#customErrorsBody')

    '''Check the input validation'''
    @property
    def validation_input(self):
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        self.add_btn_loc.click()
        msg_error = self.validation_msgbox_loc.inner_text()
        print(msg_error)
        return msg_error

    '''Input the necessary details for a door'''
    def add_custom_detail(self):
        # 选择安装类型
        self.packaging_type_select.select_option(label='Wrapped')
        self.install_type_select.select_option(label='Residential')
        self.design_select.select_option(label='Aliwood')
        self.colour_category_select.select_option(label='OilColour')
        self.opensize_lh_select.fill('2800')
        self.opensize_rh_select.fill( '2800')
        self.opensize_width_select.fill('5510')
        self.sr_left_select.fill('200')
        self.hr_select.fill( '400')
        self.sr_right_select.fill( '200')
        self.panel_wide_btn_loc.click()
        self.panel_wide_input_loc.fill('1 Panel Wide')
        self.opener_select.select_option(label='Lock Only')
        self.add_door_btn.scroll_into_view_if_needed()
        self.add_btn_loc.click(force=True)
        self.page.wait_for_timeout(2000)


    @property
    def new_added_custom_door(self):
        door_title = self.new_door_title.inner_text()
        print(door_title)
        return door_title

    @property
    def duplicate_btn(self):
        door_deplicate = self.new_door_duplicate
        if door_deplicate.is_visible():
            print('true')
            return True
        else:
            print('false')
            return False

    @property
    def delete_btn(self):
        door_delete = self.new_door_delete
        if door_delete.is_visible():
            print('true')
            return True
        else:
            print('false')
            return False

if __name__ == "__main__":
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page(viewport={"width": 2560, "height": 1440})  #
        # page = browser.new_page()
        page.goto("http:// ")
        login = Add_Custom_Door(page)
        login.typeUserName('aabb')
        login.typePassword('aabb')
        login.clicklogin()
        page.wait_for_timeout(2000)
        login.go_addquote()
        login.go_addcustomdoor()
        # login.validation_input
        login.add_custom_detail()
        login.new_added_custom_door







