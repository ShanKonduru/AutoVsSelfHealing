from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

import time
import unittest

class CustomTestLoader(unittest.TestLoader):
    def getTestMethodNames(self, testCaseClass):
        testMethodNames = super().getTestMethodNames(testCaseClass)
        return testMethodNames
