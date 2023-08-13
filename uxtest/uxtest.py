from selenium import webdriver
import time
import unittest

class TestUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Change to appropriate WebDriver

    def test_addition(self):
        self.driver.get("http://localhost:8888/ux")  # Change the URL as needed

        num1_input = self.driver.find_element_by_id("num1")
        num2_input = self.driver.find_element_by_id("num2")
        add_button = self.driver.find_element_by_id("addBtn")

        num1_input.send_keys("5")
        num2_input.send_keys("3")
        add_button.click()

        result_label = self.driver.find_element_by_id("resultLabel")
        result_text = result_label.text
        self.assertEqual(result_text, "Result: 8")

    def test_subtraction(self):
        self.driver.get("http://localhost:8888/ux")  # Change the URL as needed

        num1_input = self.driver.find_element_by_id("num1")
        num2_input = self.driver.find_element_by_id("num2")
        add_button = self.driver.find_element_by_id("subtractBtn")

        num1_input.send_keys("5")
        num2_input.send_keys("3")
        add_button.click()

        result_label = self.driver.find_element_by_id("resultLabel")
        result_text = result_label.text
        self.assertEqual(result_text, "Result: 2")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
