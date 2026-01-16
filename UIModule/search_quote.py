# Author:Yi Sun(Tim) 2025-11-19

'''Search Quote Page'''

from playwright.sync_api import Page,expect
from UIModule.admin_portal import Admin_Page

class Search_Quote(Admin_Page):

    def __init__(self,page:Page):
        super().__init__(page)
        self._init_locators_search_quote()

    def _init_locators_search_quote(self):
        '''loc for default values in this page'''
        self.searchquote_title_loc = self.page.locator("[name='searchquote']")
        self.quotes_sub_loc = self.page.locator("[aria-label='quotes_sub']")
        self.doors_sub_loc = self.page.locator("[aria-label='doors_sub']")
        self.searchresult_loc = self.page.locator("[aria-label='search_result']")

        '''loc for default values in "Quotes" section'''
        self.date_range_loc = self.page.locator("[aria-label='date_range']")
        self.client_details_loc = self.page.locator("[aria-label='client_details']")
        self.quote_info_loc = self.page.locator("[aria-label='quote_info']")
        self.searchquotes_btn_loc = self.page.locator('#btnSearchQuote')
        self.filter_date_loc = self.page.locator("[aria-label='filter_date']")
        self.user_loc = self.page.locator("[aria-label='user']")
        self.user_box_loc = self.page.locator('xpath=//*[@id="UserAssignedId"]')
        self.quote_status_loc = self.page.locator("[aria-label='quote_status']")
        self.client_name_loc = self.page.locator("[aria-label='client_name']")
        self.contact_number_loc = self.page.locator("[aria-label='contact_number']")
        self.suburb_loc = self.page.locator("[aria-label='suburb']")
        self.postcode_loc = self.page.locator("[aria-label='postcode']")

        self.proposal_no_loc = self.page.locator("[aria-label='proposal_no']")
        self.door_design_loc = self.page.locator("[aria-label='door_design']")
        self.colour_category_loc = self.page.locator("[aria-label='colour_category']")
        self.door_colour_loc = self.page.locator("[aria-label='door_colour']")
        self.site_address_loc = self.page.locator("[aria-label='site_address']")

        '''Input box for each filter'''
        self.clientname_box_loc = self.page.locator('#ClientName')
        self.proposal_no_box_loc = self.page.locator('#ProposalNo')
        self.contact_num_box_loc = self.page.locator('#Contact_Number')
        self.suburb_box_loc = self.page.locator('#Suburb')
        self.postcode_box_loc = self.page.locator('#Postcode')
        self.door_design_select_loc = self.page.locator('#DoorDesign')
        self.door_colour_select_loc = self.page.locator('#DoorColor')
        self.door_category_select_loc = self.page.locator('#ColourCategory')
        self.site_address_box_loc = self.page.locator('#SiteAddress')

        '''search by client name'''
        self.proposalno_searched_loc = self.page.locator("[aria-label='proposalno_searched']")


    def go_searchquotes(self):
        '''Switch to Search Quotes from LIST Menu'''
        self.list_loc.click()
        self.quote_list_loc.click()
        self.searchquote_title_loc.wait_for()

    @property
    def check_title(self):
        '''check the title for Search Quotes page'''
        searchquote_title = self.searchquote_title_loc.inner_text()
        print(searchquote_title)
        return searchquote_title

    @property
    def check_searchurl(self):
        '''check the url for Search Quotes page'''
        searchquotes_url = self.page.url
        print(searchquotes_url)
        return searchquotes_url

    @property
    def check_defaulsection(self):
        '''check the default section in Search Quotes page'''
        searchquote_btn = self.searchquotes_btn_loc.is_enabled()
        if searchquote_btn:
            print('exist')
            return True
        else:
            print("not exist")
            return False

    @property
    def check_defaultelements(self):
        '''check the default elements in Search Quotes page'''
        quotes_sub = self.quotes_sub_loc.inner_text()
        doors_sub = self.doors_sub_loc.inner_text()
        search_result = self.searchresult_loc.inner_text()
        print(quotes_sub, doors_sub, search_result)
        return quotes_sub, doors_sub, search_result

    @property
    def check_section_quotes(self):
        '''check each section of Quotes filter table in Search Quotes page'''
        date_range = self.date_range_loc.inner_text()
        client_details = self.client_details_loc.inner_text()
        quote_info = self.quote_info_loc.inner_text()
        print(date_range, client_details, quote_info)
        return date_range, client_details, quote_info

    @property
    def check_date_range(self):
        '''check each filter in "Date Range" in Quotes filter table'''
        filter_date = self.filter_date_loc.inner_text()
        user =self.user_loc.inner_text()
        quote_status = self.quote_status_loc.inner_text()
        print(filter_date, user, quote_status)
        return filter_date, user, quote_status

    @property
    def check_client_details(self):
        '''check each filter in "Client Details" in Quotes filter table'''
        client_name = self.client_name_loc.inner_text()
        contact_number = self.contact_number_loc.inner_text()
        suburb = self.suburb_loc.inner_text()
        postcode = self.postcode_loc.inner_text()
        print(client_name, contact_number, suburb, postcode)
        return client_name, contact_number, suburb, postcode

    @property
    def check_quote_info(self):
        '''check each filter in "Quote Infomation" in Quotes filter table'''
        proposal_no = self.proposal_no_loc.inner_text()
        door_design = self.door_design_loc.inner_text()
        colour_category = self.colour_category_loc.inner_text()
        door_colour = self.door_colour_loc.inner_text()
        site_address = self.site_address_loc.inner_text()
        print(proposal_no, door_design, colour_category, door_colour, site_address)
        return proposal_no, door_design, colour_category, door_colour, site_address

    @property
    def check_default_user(self):
        '''check the default user name in "User" filter in Quotes filter table'''
        default_user = self.user_box_loc.evaluate("select=>select.options[select.selectedIndex].textContent").strip()
        print(default_user)
        return default_user

    @property
    def search_client_name(self):
        '''check the search by client name function'''
        self.clientname_box_loc.fill('Test Automation')
        self.page.wait_for_timeout(3000)
        self.searchquotes_btn_loc.click()
        # self.page.wait_for_timeout(3000)
        searched_proposalno = self.proposalno_searched_loc.inner_text()
        self.clientname_box_loc.clear()
        print(searched_proposalno)
        return searched_proposalno

    @property
    def search_proposal_id(self):
        '''check the search by Proposal ID function'''
        self.proposal_no_box_loc.fill('210088')
        self.page.wait_for_timeout(3000)
        self.searchquotes_btn_loc.click()
        searched_proposalno = self.proposalno_searched_loc.inner_text()
        self.proposal_no_box_loc.clear()
        print(searched_proposalno)
        return searched_proposalno

    @property
    def search_contact_num(self):
        '''check the search by Contact Number function'''
        self.contact_num_box_loc.fill('046999999')
        self.page.wait_for_timeout(3000)
        self.searchquotes_btn_loc.click()
        searched_proposalno = self.proposalno_searched_loc.inner_text()
        self.contact_num_box_loc.clear()
        print(searched_proposalno)
        return searched_proposalno

    @property
    def search_suburb(self):
        '''check the search by Suburb function'''
        self.suburb_box_loc.fill('BURWOOD EAST')
        self.page.wait_for_timeout(3000)
        self.searchquotes_btn_loc.click()
        searched_proposalno = self.proposalno_searched_loc.inner_text()
        self.suburb_box_loc.clear()
        print(searched_proposalno)
        return searched_proposalno

    @property
    def search_postcode(self):
        '''check the search by Postcode function'''
        self.postcode_box_loc.fill('3151')
        self.page.wait_for_timeout(3000)
        self.searchquotes_btn_loc.click()
        searched_proposalno = self.proposalno_searched_loc.inner_text()
        self.postcode_box_loc.clear()
        print(searched_proposalno)
        return searched_proposalno

    @property
    def search_door_design(self):
        '''check the search by Door Design function'''
        self.page.wait_for_timeout(5000)
        self.door_design_select_loc.select_option(label='Wideline')
        self.page.wait_for_timeout(3000)
        self.searchquotes_btn_loc.click()
        searched_proposalno = self.proposalno_searched_loc.inner_text()
        self.door_design_select_loc.select_option(index=0)
        print(searched_proposalno)
        return searched_proposalno

    @property
    def search_door_colour(self):
        '''check the search by Door Colour function'''
        self.page.wait_for_timeout(5000)
        self.door_colour_select_loc.select_option(label='Wallaby')
        self.page.wait_for_timeout(3000)
        self.searchquotes_btn_loc.click()
        searched_proposalno = self.proposalno_searched_loc.inner_text()
        self.door_colour_select_loc.select_option(index=0)
        self.page.wait_for_timeout(3000)
        print(searched_proposalno)
        return searched_proposalno

    @property
    def search_door_category(self):
        '''check the search by Colour Category function'''
        self.page.wait_for_timeout(5000)
        self.door_category_select_loc.select_option(label='Timber Essence')
        self.searchquotes_btn_loc.click()
        searched_proposalno = self.proposalno_searched_loc.inner_text()
        self.door_category_select_loc.select_option(index=0)
        print(searched_proposalno)
        return searched_proposalno

    @property
    def search_site_address(self):
        '''check the search by Site Address function'''
        self.site_address_box_loc.fill('Automation')
        self.searchquotes_btn_loc.click()
        self.proposalno_searched_loc.inner_text()
        self.postcode_box_loc.clear()
        print(searched_proposalno)
        return searched_proposalno


if __name__ == "__main__":
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 2560, "height": 1440}, ignore_https_errors=True)
        page = context.new_page()
        page.goto("http:// ")
        login = Search_Quote(page)
        login.typeUserName('aabb')
        login.typePassword('aabb')
        login.clicklogin()
        page.wait_for_timeout(2000)
        login.go_searchquotes()
        # login.check_searchurl
        # login.check_title
        login.check_defaulsection
        # login.check_defaultvalue
        # login.check_defaultelements
        # login.check_section_quotes
        # login.check_date_range
        # login.check_client_details
        # login.check_quote_info
        # login.check_default_user
        login.search_client_name
        # login.search_proposal_id
        # login.search_contact_num
        # login.search_door_design
        login.search_door_colour
        # login.search_door_category
        # login.search_suburb
        # login.search_postcode
        # login.search_site_address
