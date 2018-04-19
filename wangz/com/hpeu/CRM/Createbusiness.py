import unittest
import time
from selenium import webdriver
from hpeu.Tools.ReadFile import ReadFile
from hpeu.CRM.Login import Login
from hpeu.Tools.GetScreenshot import GetScreenshot
class Createbusiness(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.getValue = ReadFile()
        self.getscreenshotTest = GetScreenshot(self.driver)
    def test_Createbusiness(self):
        Login.test_Login(self)
        time.sleep(5)
        
        Createbusinesslink = self.getValue.getElement("XPATH","Createbusinesslink")
        BusinessName = self.getValue.getElement("XPATH", "BusinessName")
        Estimate_price = self.getValue.getElement("XPATH", "Estimate_price")
        CreatebusinessBtn = self.getValue.getElement("XPATH", "CreatebusinessBtn")
        IBusinessName =self.getValue.getInputValue("Createbusiness", "IBusinessName")
        IEstimate_price = self.getValue.getInputValue("Createbusiness", "IEstimate_price")
        
        
        self.driver.find_element_by_xpath(Createbusinesslink).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(BusinessName).send_keys(IBusinessName)
        self.driver.find_element_by_xpath(Estimate_price).send_keys(IEstimate_price)
        
        self.driver.find_element_by_xpath(CreatebusinessBtn).click()
        
        time.sleep(5)
        self.getscreenshotTest.screenshot("Createbusiness")
    def tearDown(self):
        Login.tearDown(self)

    if __name__ == "__main__":
        unittest.main()