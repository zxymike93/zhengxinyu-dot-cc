#! /usr/bin/pyhon3

import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(7)

    def tearDown(self):
        self.browser.quit()

    def test_can_see_title(self):
        self.browser.get('http://0.0.0.0:80')
        self.assertIn('Mike', self.browser.title)
        self.fail('Finish test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
