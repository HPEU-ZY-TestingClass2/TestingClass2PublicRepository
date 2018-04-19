import unittest
import time
from selenium import webdriver
from hpeu.CRM.Login import Login
from hpeu.Tools.ReadFile import ReadFile
from hpeu.Tools.GetScreenshot import GetScreenshot

class LookCustomer(unittest.TestCase):
    def setUp(self):
        self.driver =webdriver.Firefox()
        self.getValue = ReadFile()
        self.getscreenshotTest = GetScreenshot(self.driver)
    def test_LookCustomer(self):
        Login.test_Login(self)
        time.sleep(5)
        
        LookCustomerlink = self.getValue.getElement("XPATH", "LookCustomerlink")
        
        
        self.driver.find_element_by_xpath(LookCustomerlink).click()
        time.sleep(5)
        self.getscreenshotTest.screenshot("LookCustomeer")
    def tearDown(self):
        Login.tearDown(self)
        
    if "__name__" == "__main__":
        unittest.main()