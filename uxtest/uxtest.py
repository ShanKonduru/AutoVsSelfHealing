import pytest
import pytest_html

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from CustomTestLoader import CustomTestLoader

import time
import unittest
import logging


class TestUI(unittest.TestCase):
    def setUp(self):
        # Create a WebDriver instance (example using Chrome)
        self.driver = Chrome()

    def test_addition(self):
        extras.text("test_addition")
        self.driver.get("http://localhost:8888/ux")  # Change the URL as needed
        time.sleep(2)
        num1_input = self.driver.find_element(By.ID, "num1")
        num2_input = self.driver.find_element(By.ID, "num2")
        add_button = self.driver.find_element(By.ID, "addBtn")
        extras.text("got num1, num2 addBtn")
        time.sleep(2)
        num1_input.send_keys("5")
        num2_input.send_keys("3")
        add_button.click()
        extras.text("Add num1 and num2")
        time.sleep(2)
        result_label = self.driver.find_element(By.ID, "resultLabel")
        result_text = result_label.text
        self.assertEqual(result_text, "Result: 8")
        extras.text("result updated")

    def test_subtraction(self):
        extras.text("Subtract started")
        self.driver.get("http://localhost:8888/ux")  # Change the URL as needed
        time.sleep(2)
        num1_input = self.driver.find_element(By.ID, "num1")
        num2_input = self.driver.find_element(By.ID, "num2")
        add_button = self.driver.find_element(By.ID, "subtractBtn")
        extras.text("Got num1, num2, Subtract")
        time.sleep(2)
        num1_input.send_keys("5")
        num2_input.send_keys("3")
        add_button.click()
        extras.text("Subtract num1 and num2")
        time.sleep(2)
        result_label = self.driver.find_element(By.ID, "resultLabel")
        result_text = result_label.text
        self.assertEqual(result_text, "Result: 2")
        extras.text("result updated")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    # Set up logging configuration
    logging.basicConfig(level=logging.INFO)
    pytest.main(
        [
            "uxtest.py",
            "--html=ux-test-report.html",
            "--self-contained-html",  # Optional: Generate a single self-contained HTML file
            "--show-capture=all",  # Optional: Show captured output in the console
        ]
    )
