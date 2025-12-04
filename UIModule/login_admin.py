# Author:Yi Sun(Tim) 2025-10-16

'''Login Page'''

from playwright.sync_api import sync_playwright
from UIModule.basepage import *

class Admin_Portal(WebDriver):
    username_loc = 'xpath=//*[@id="Email"]'
    password_loc = 'xpath=//*[@id="Password"]'
    login_loc = 'xpath=//*[@id="loginForm"]/form/div[4]/div/input'

    def __init__(self,page):
        self.page = page
        super().__init__(page)

    def typeUserName(self,username):
        self.page.fill(self.username_loc,username)

    def typePassword(self,password):
        self.page.fill(self.password_loc,password)

    def clicklogin(self):
        self.page.click(self.login_loc)

    def login(self,username, password):
        self.typeUserName(username)
        self.typePassword(password)

    def getUsername(self):
        username_text = self.page.text_content(self.username_loc)
        print('username is:', username_text)
        return username_text
