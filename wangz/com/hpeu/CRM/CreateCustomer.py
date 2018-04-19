import unittest
import time
from selenium import webdriver
from hpeu.Tools.ReadFile import ReadFile
from hpeu.CRM.Login import Login
from hpeu.Tools.GetScreenshot import GetScreenshot

class CreateCustomer(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.getValue = ReadFile()
        self.getscreenshotTest = GetScreenshot(self.driver)
    def test_CreateCustomer(self):
        Login.test_Login(self)
        CreateCustomerlink =self.getValue.getElement("XPATH", "CreateCustomerlink")
        KfName = self.getValue.getElement("XPATH", "KfName")
        KfBcBtn = self.getValue.getElement("XPATH", "KfBcBtn")
        IKfName = self.getValue.getInputValue("CreateCustomer", "KfName")
        time.sleep(20)
        
        self.driver.find_element_by_xpath(CreateCustomerlink).click()
        self.driver.find_element_by_xpath(KfName).send_keys(IKfName)
        self.driver.find_element_by_xpath(KfBcBtn).click()
        
        time.sleep(5)
        self.getscreenshotTest.screenshot("Createcustomer")
    def tearDown(self):
        Login.tearDown(self)

    if __name__ == "__main__":
        unittest.main()