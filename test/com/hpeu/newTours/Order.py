import unittest
import time
from hpeu.newTours.Search import SearchTest
from selenium import webdriver
from hpeu.Tools.ReadFile import ReadFile
from hpeu.Tools.GetScreenshot import GetScreenshot
class OrderTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.getValue=ReadFile()
        self.getScreenTest = GetScreenshot(self.driver)
    def test_OrderTest(self):
        mydriver = self.driver
        SearchTest.test_SearchTest(self)
        
        FName = self.getValue.getElement("XPATH", "FName")
        LName = self.getValue.getElement("XPATH", "LName")
        Number = self.getValue.getElement("XPATH", "Number")
        SP = self.getValue.getElement("XPATH", "SP")
        Ifname = self.getValue.getInputValue("Order", "FName")
        ILname = self.getValue.getInputValue("Order", "LName")
        Inumber = self.getValue.getInputValue("Order", "Number")
        
        
        mydriver.find_element_by_xpath(FName).send_keys(Ifname)
        mydriver.find_element_by_xpath(LName).send_keys(ILname)
        mydriver.find_element_by_xpath(Number).send_keys(Inumber)
        mydriver.find_element_by_xpath(SP).click()
        
        time.sleep(5)
        self.getScreenTest.screenshot("Order")
        
    def tearDown(self):
        SearchTest.tearDown(self)
        
    if __name__ == '__main__':
        unittest.main()