# Author:Yi Sun(Tim) 2025-10-28

'''Test Admin Portal Page by Pytest'''

from playwright.sync_api import Page
import pytest
from UIModule.admin_portal import Admin_Page


class TestAdminPortal:

    @pytest.fixture(autouse=True)
    def setup(self,page:Page):
        self.page = page
        self.admin_page = Admin_Page(page)
        page.goto("http://egd2.sighte.com/")
        self.admin_page.typeUserName('ysun@ecogaragedoors.com.au')
        self.admin_page.typePassword('Tims@123')
        self.admin_page.clicklogin()

    def test_get_url(self):
        current_url = self.admin_page.getURL
        assert "http://aabb/" in current_url

    def test_check_default_menu(self):
        assert ('ADD','LIST','ACCOUNT') in self.admin_page.check_defaultmenu

    def test_check_find_quote(self):
        assert self.admin_page.check_findquote is True

    def test_check_find_client(self):
        assert self.admin_page.check_findclient is True

    def test_check_copyright(self):
        assert ('© 2025 - EcoGarageDoors','Terms and Policies') in self.admin_page.check_copyright


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s", "--headed"])