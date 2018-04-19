import unittest
import time
from selenium import webdriver
from hpeu.Tools.ReadFile import ReadFile
from hpeu.CRM.Login import Login
from hpeu.Tools.GetScreenshot import GetScreenshot
class Looktask(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.getValue = ReadFile()
        self.getscreenshotTest = GetScreenshot(self.driver)
    def test_Looktask(self):
        Login.test_Login(self)
        time.sleep(5)
        
        Looktasklink = self.getValue.getElement("XPATH", "Looktasklink")
        
        self.driver.find_element_by_xpath(Looktasklink).click()
        time.sleep(5)
        self.getscreenshotTest.screenshot("Looktask")
    def tearDown(self):
        Login.tearDown(self)
        
    if __name__ == "__maIN__":
        unittest.main()