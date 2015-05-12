# -*- coding: utf-8 -*-
from selenium.webdriver.firefox import webdriver
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class HomeNewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.WebDriver()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    def test_home_title(self):
        self.browser.get(self.get_full_url("home"))
        self.assertIn("SDH Svinov", self.browser.title)


if __name__ == "__main__":
    unittest.main(warnings='ignore')
