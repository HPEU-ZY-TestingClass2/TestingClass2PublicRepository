
import unittest
from selenium import webdriver
import time
from hpeu.Tools.ReadFile import ReadFile
from hpeu.Tools.GetScreenshot import GetScreenshot
class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.getValue = ReadFile()
        self.getscreenshotTest = GetScreenshot(self.driver)
    def test_Login(self):
        mydriver = self.driver
        
        URL = self.getValue.getURL("SystemURL", "URL")
        mydriver.get(URL)
        
        UserName = self.getValue.getElement("XPATH", "Name")
        UserPassword = self.getValue.getElement("XPATH", "Password")
        LoginBtn = self.getValue.getElement("XPATH", "Loginbtn")
        IName = self.getValue.getInputValue("Login", "InputName")
        Ipassword = self.getValue.getInputValue("Login", "Inputpassword")
        
        
        self.driver.find_element_by_xpath(UserName).send_keys(IName)
        self.driver.find_element_by_xpath(UserPassword).send_keys(Ipassword)
        self.driver.find_element_by_xpath(LoginBtn).click()
        
        
        time.sleep(2)
        self.getscreenshotTest.screenshot("Login")
        
    def tearDown(self):
        self.driver.close()
        
    if __name__ == '__main__':
        unittest.main()
    
        