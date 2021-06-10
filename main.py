import unittest

from selenium import webdriver
browser=webdriver.Edge('msedgedriver.exe')
browser.get('http://localhost:8000')
assert '88' in browser.title,"Browser title was"+browser.title

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Edge('msedgedriver.exe')

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Django',self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')