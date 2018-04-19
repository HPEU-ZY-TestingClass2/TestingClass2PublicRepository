import unittest
import time
from selenium import webdriver
from hpeu.Tools.ReadFile import ReadFile
from hpeu.CRM.Login import Login
from hpeu.Tools.GetScreenshot import GetScreenshot
class Lookschedule(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.getValue = ReadFile()
        self.getscreenshotTest = GetScreenshot(self.driver)
    def test_Lookschedule(self):
        Login.test_Login(self)
        time.sleep(15)
        Lookschedulelink = self.getValue.getElement("XPATH", "Lookschedulelink")
        
        self.driver.find_element_by_xpath(Lookschedulelink).click()
        time.sleep(15)
        self.getscreenshotTest.screenshot("Lookscheddule")
    def tearDown(self):
        Login.tearDown(self)

    if __name__ == "__main__":
        unittest.main()