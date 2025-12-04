# Author:Yi Sun(Tim) 2025-10-16

'''Base Page'''

from playwright.sync_api import sync_playwright,TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import Page

class Factory(object):
    def __init__(self,page):
        self.page = page

    def createDriver(self,driver_type):
        if driver_type == 'web':
            return WebUI(self.page)
        elif driver_type == 'app':
            return AppUI(self.page)
        else:
            raise ValueError(f"Unsupported driver type:{driver_type}")

class WebDriver(object):
    def __init__(self,page):
        self.page = page

    def findElement(self,selector,timeout = 20000):
        try:
            element = self.page.wait_for_selector(selector,timeout=timeout)
            return element
        except PlaywrightTimeoutError as e:
            print(f'Error Details: Element not found with selector "{selector}"')
            print(f'Timeout after {timeout}ms')
            return None

    def findElements(self, selector, timeout=20000):
        '''Multiple Elements locate with Playwright'''
        try:
            self.page.wait_for_selector(selector, timeout=timeout)
            return self.page.query_selector_all(selector)
        except PlaywrightTimeoutError as e:
            print(f'Error Details: No elements found with selector "{selector}"')
            return []

    def click(self, selector, timeout=20000):
        '''Click element with automatic waiting'''
        try:
            self.page.click(selector, timeout=timeout)
            return True
        except PlaywrightTimeoutError as e:
            print(f'Error Details: Cannot click element "{selector}"')
            return False

    def fill(self, selector, text, timeout=20000):
        '''Fill input field with automatic waiting'''
        try:
            self.page.fill(selector, text, timeout=timeout)
            return True
        except PlaywrightTimeoutError as e:
            print(f'Error Details: Cannot fill element "{selector}" with text "{text}"')
            return False

    def get_text(self, selector, timeout=20000):
        '''Get text content of element'''
        try:
            element = self.findElement(selector, timeout)
            if element:
                return element.text_content()
            return None
        except Exception as e:
            print(f'Error getting text from "{selector}": {e}')
            return None

class WebUI(WebDriver):
    def __init__(self, page):
        super().__init__(page)
        pass

    def navigate_to(self, url):
        '''Navigate to URL'''
        try:
            self.page.goto(url)
            return True
        except Exception as e:
            print(f'Error navigating to {url}: {e}')
            return False

    def get_page_title(self):
        '''Get current page title'''
        return self.page.title()

    def take_screenshot(self, path='screenshot.png'):
        '''Take screenshot'''
        try:
            self.page.screenshot(path=path)
            return True
        except Exception as e:
            print(f'Error taking screenshot: {e}')
            return False

class AppUI(WebDriver):
    def __init__(self, page):
        super().__init__(page)
        pass

    def tap(self, selector):
        '''模拟移动端点击'''
        return self.click(selector)

    def swipe(self, direction='up'):
        '''模拟滑动操作'''
        try:
            viewport_size = self.page.viewport_size
            if direction == 'up':
                self.page.mouse.wheel(0, -300)
            elif direction == 'down':
                self.page.mouse.wheel(0, 300)
            return True
        except Exception as e:
            print(f'Error swiping {direction}: {e}')
            return False
