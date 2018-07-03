from selenium import webdriver
import unittest

class LinkScreenshots(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://")

    def test_link_screenshots_soft(self):
        self.assertIn("Квест ассистента менеджера", self.driver.title)
        link = self.driver.find_element_by_link_text('НАХОДИТЬ НЕСОВЕРШЕНСТВА')
        link.click()
        link = self.driver.find_element_by_link_text('Софт для быстрого создания скриншотов')
        href = link.get_attribute("href")
        self.assertEqual(href, 'http://monosnap.com/')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
