"""
Copyright (c) 2023 Plugin Andrey (9keepa@gmail.com)
Licensed under the MIT License
"""
import unittest
import logging
from web_render.base.abstract import make_selenium_webdriver, SeleniumRender
from functools import partial
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
logging.disable(logging.WARNING)
# import sys
# sys.stderr = open("test_error.log", 'a')

CHROME_DRIVER_VERSION = "123.0.6312.105"

class TestServices(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.partial_browser = partial(make_selenium_webdriver)

    def setUp(self):
        pass

    def test_01(self):
        with SeleniumRender(self.partial_browser({"CHROME_DRIVER_VERSION":CHROME_DRIVER_VERSION})) as render:
            render.set_url("https://2ip.ru")
            self.assertTrue(len(render.browser.find_elements(By.CSS_SELECTOR, 'script')))

    def test_02(self):
        with SeleniumRender(self.partial_browser({"CHROME_DRIVER_VERSION":CHROME_DRIVER_VERSION})) as render:
            render.set_url("https://www.ozon.ru/category/smartfony-15502/", web_wait={
                    "name": "CheckNumberElementsInPage",
                    "params": {
                        "selector":"[data-widget=searchResultsV2] a.tile-hover-target[data-prerender]",
                        "count": 30
                    }
                }
            )
            self.assertTrue("ozon" in render.browser.title.lower())
            self.assertTrue(36>=len(render.browser.find_elements(By.CSS_SELECTOR, "[data-widget=searchResultsV2] a.tile-hover-target[data-prerender]")))

            with self.assertRaises(TimeoutException):
                render.set_url("https://www.ozon.ru/category/sistemnye-bloki-15704/", web_wait={
                        "name": "CheckNumberElementsInPage",
                        "params": {
                            "selector":"[data-widget=searchResultsV2] a.tile-hover-target[data-prerender]",
                            "count": 36
                        }
                    }
                )


    def test_03_undetected(self):
        with SeleniumRender(self.partial_browser({
            "CHROME_DRIVER_VERSION":CHROME_DRIVER_VERSION,
            "UNDETECTED_CHROMEDRIVER": True,
            "HEADLESS": False
        })) as render:
            render.set_url("https://www.ozon.ru/category/smartfony-15502/", web_wait={
                    "name": "CheckNumberElementsInPage",
                    "params": {
                        "selector":"[data-widget=searchResultsV2] a.tile-hover-target[data-prerender]",
                        "count": 30
                    }
                }
            )
            self.assertTrue(30<=len(render.browser.find_elements(By.CSS_SELECTOR, "[data-widget=searchResultsV2] a.tile-hover-target[data-prerender]")))

            render.set_url("https://www.ozon.ru/category/futbolnaya-forma-37350/", web_wait={
                    "name": "CheckNumberElementsInPage",
                    "params": {
                        "selector":"[data-widget=searchResultsV2] a.tile-hover-target[data-prerender]",
                        "count": 30
                    }
                }
            )
            self.assertTrue(30<=len(render.browser.find_elements(By.CSS_SELECTOR, "[data-widget=searchResultsV2] a.tile-hover-target[data-prerender]")))

    def test_04(self):

        auth_proxy = "168.196.237.197:9183@DbMPBg:PE5xjW"
        with SeleniumRender(self.partial_browser({
            "CHROME_DRIVER_VERSION":CHROME_DRIVER_VERSION,
            "AUTH_PROXY_SERVER": auth_proxy
        })) as render:
            render.set_url("https://2ip.ru")
            res = render.browser.find_element(By.CSS_SELECTOR, "#d_clip_button span").text
            self.assertTrue(res in auth_proxy)

    @classmethod
    def tearDownClass(cls):
        pass

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestServices('test_login_action'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
