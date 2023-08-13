from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from CustomTestLoader import CustomTestLoader

import time
import unittest

class TestUI(unittest.TestCase):
    def setUp(self):
        # chrome_driver_path = './chromedriver.exe'  # Update this path
        # chrome_options = webdriver.ChromeOptions()
        # Add any desired options to chrome_options here
        # For example, to run Chrome in headless mode:
        # chrome_options.add_argument('--headless')

        # Create Chrome WebDriver instance using options
        # self.driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
        # self.driver = webdriver.Chrome(options=chrome_options)
        # self.driver = webdriver.Chrome()

        # Create a WebDriver instance (example using Chrome)
        self.driver = Chrome()

    def test_addition(self):
        self.driver.get("http://localhost:8888/ux")  # Change the URL as needed
        time.sleep(2)
        num1_input = self.driver.find_element(By.ID, "num1")
        num2_input = self.driver.find_element(By.ID, "num2")
        add_button = self.driver.find_element(By.ID, "addBtn")
        time.sleep(2)
        num1_input.send_keys("5")
        num2_input.send_keys("3")
        add_button.click()
        time.sleep(2)
        result_label = self.driver.find_element(By.ID, "resultLabel")
        result_text = result_label.text
        self.assertEqual(result_text, "Result: 8")

    def test_subtraction(self):
        self.driver.get("http://localhost:8888/ux")  # Change the URL as needed
        time.sleep(2)
        num1_input = self.driver.find_element(By.ID, "num1")
        num2_input = self.driver.find_element(By.ID, "num2")
        add_button = self.driver.find_element(By.ID, "subtractBtn")
        time.sleep(2)
        num1_input.send_keys("5")
        num2_input.send_keys("3")
        add_button.click()
        time.sleep(2)
        result_label = self.driver.find_element(By.ID, "resultLabel")
        result_text = result_label.text
        self.assertEqual(result_text, "Result: 2")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    test_loader = CustomTestLoader()
    test_suite = unittest.TestSuite()

    # Add your test cases here
    test_suite.addTest(TestUI("test_addition"))
    test_suite.addTest(TestUI("test_subtraction"))

    # Use the built-in HTMLTestRunner
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)

    # Generate the HTML report
    with open("test_report.html", "w") as report_file:
        runner = unittest.HTMLTestRunner(
            stream=report_file,
            title="UI Test Report",
            description="Test results for UI functionality"
        )
        runner.run(test_suite)
