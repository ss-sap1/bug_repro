from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time


class TestDoubleClick(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://blog.csssr.ru/qa-engineer")

    def test_double_click(self):
        driver = self.driver

        graphs = driver.find_element_by_class_name("graphs")
        driver.execute_script("arguments[0].scrollIntoView()", graphs)
        time.sleep(5)

        tab = driver.find_element_by_css_selector(".graphs-errors>a")
        ActionChains(driver).double_click(tab).perform()
        time.sleep(3)

        driver.save_screenshot("DoubleClick.png")
        link = driver.find_element_by_link_text("Софт для быстрого создания скриншотов")
        link.click()


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()