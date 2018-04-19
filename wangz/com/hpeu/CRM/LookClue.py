import unittest
import time
from selenium import webdriver
from hpeu.Tools.ReadFile import ReadFile
from hpeu.CRM.Login import Login
from hpeu.Tools.GetScreenshot import GetScreenshot
class LookClue(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.getValue = ReadFile()
        self.getscreenshotTest = GetScreenshot(self.driver)
    def test_LookClue(self):
        Login.test_Login(self)
        time.sleep(5)
        LookClueLink = self.getValue.getElement("XPATH", "LookClueLink")
        
        self.driver.find_element_by_xpath(LookClueLink).click()
        time.sleep(5)
        self.getscreenshotTest.screenshot("LookClue")
    def tearDown(self):
        Login.tearDown(self)
        
    if "__name__" == "__main__":
        unittest.main()