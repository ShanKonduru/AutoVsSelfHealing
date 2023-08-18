import pytest
import pytest_html

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from CustomTestLoader import CustomTestLoader
from logging  import FileHandler, Formatter

import time
import unittest
import logging


class TestUI(unittest.TestCase):
    def setUp(self):
        # Create a WebDriver instance (example using Chrome)
        self.driver = Chrome()

    def test_addition(self):
        log = logging.getLogger(__name__)
        log.info("test_addition")
        self.driver.get("http://localhost:8888/app/ux")  # Change the URL as needed
        time.sleep(2)
        num1_input = self.driver.find_element(By.ID, "num1")
        num2_input = self.driver.find_element(By.ID, "num2")
        add_button = self.driver.find_element(By.ID, "addBtn")
        log.info("got num1, num2 addBtn")
        time.sleep(2)
        num1_input.send_keys("5")
        num2_input.send_keys("3")
        add_button.click()
        log.info("Add num1 and num2")
        time.sleep(2)
        result_label = self.driver.find_element(By.ID, "resultLabel")
        result_text = result_label.text
        self.assertEqual(result_text, "Result: 8")
        log.info("result updated")

    def test_subtraction(self):
        log = logging.getLogger(__name__)
        log.info("Subtract started")
        self.driver.get("http://localhost:8888/app/ux")  # Change the URL as needed
        time.sleep(2)
        num1_input = self.driver.find_element(By.ID, "num1")
        num2_input = self.driver.find_element(By.ID, "num2")
        add_button = self.driver.find_element(By.ID, "subtractBtn")
        log.info("Got num1, num2, Subtract")
        time.sleep(2)
        num1_input.send_keys("5")
        num2_input.send_keys("3")
        add_button.click()
        log.info("Subtract num1 and num2")
        time.sleep(2)
        result_label = self.driver.find_element(By.ID, "resultLabel")
        result_text = result_label.text
        self.assertEqual(result_text, "Result: 2")
        log.info("result updated")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    # Remove all handlers associated with the root logger object.
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # Set up logging configuration
    logging.basicConfig(
        filename=__name__,
        filemode="w",
        format="%(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
        force=True,
    )

    pytest.main(
        [
            "uxtest.py",
            "--html=ux-test-report.html",
            "--self-contained-html",  # Optional: Generate a single self-contained HTML file
            "--show-capture=all",  # Optional: Show captured output in the console
        ]
    )
