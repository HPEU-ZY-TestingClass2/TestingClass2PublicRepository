import unittest
import time
from selenium import webdriver
from hpeu.Tools.ReadFile import ReadFile
from hpeu.CRM.Login import Login
from hpeu.Tools.GetScreenshot import GetScreenshot
class Lookbusiness(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.getValue = ReadFile()
        self.getscreenshotTest = GetScreenshot(self.driver)

    def test_Lookbusiness(self):
        Login.test_Login(self)
        time.sleep(10)
        Lookbusinesslink = self.getValue.getElement("XPATH", "Lookbusinesslink")
        
        self.driver.find_element_by_xpath(Lookbusinesslink).click()
        time.sleep(15)
        self.getscreenshotTest.screenshot("Lookbusiness")
    def tearDown(self):
        Login.tearDown(self)

    if __name__ == "__main__":
        unittest.main()