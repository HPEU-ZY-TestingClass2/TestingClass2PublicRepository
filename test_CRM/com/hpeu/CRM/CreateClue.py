import unittest
import time
from selenium import webdriver
from hpeu.Tools.ReadFile import ReadFile
from hpeu.CRM.Login import Login
from hpeu.Tools.GetScreenshot import GetScreenshot
class CreateClue(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.getValue = ReadFile()
        self.getscreenshotTest = GetScreenshot(self.driver)
    def test_CreateClue(self):
        Login.test_Login(self)
        CreateClueLink = self.getValue.getElement("XPATH", "CreateClueLink")

        LxName = self.getValue.getElement("XPATH", "LxName")
        LxPhone = self.getValue.getElement("XPATH", "LxPhone")
        LXEmail = self.getValue.getElement("XPATH", "LXEmail")
        Ilxname = self.getValue.getInputValue("CreateClue", "Ilxname")
        Ilxphone = self.getValue.getInputValue("CreateClue", "Ilxphone")
        Ilxemail = self.getValue.getInputValue("CreateClue", "Ilxemail")
        
        time.sleep(5)
        self.driver.find_element_by_xpath(CreateClueLink).click()
        
        self.driver.find_element_by_xpath(LxName).send_keys(Ilxname)
        self.driver.find_element_by_xpath(LxPhone).send_keys(Ilxphone)
        self.driver.find_element_by_xpath(LXEmail).send_keys(Ilxemail)
        
        time.sleep(5)
        self.getscreenshotTest.screenshot("CreateClue")
        
    def tearDown(self):
        Login.tearDown(self)

    if __name__ == "__main__":
        unittest.main()