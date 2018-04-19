import unittest
import time
from selenium import webdriver
from hpeu.Tools.ReadFile import ReadFile
from hpeu.CRM.Login import Login
from hpeu.Tools.GetScreenshot import GetScreenshot
class Createschedule(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.getValue = ReadFile()
        self.getscreenshotTest = GetScreenshot(self.driver)
    def test_Createschedule(self):
        Login.test_Login(self)
        time.sleep(10)
        
        Createschedulelink = self.getValue.getElement("XPATH", "Createschedulelink")
        Subject = self.getValue.getElement("XPATH", "Subject")
        Description = self.getValue.getElement("XPATH", "Description")
        Createschedulebtn = self.getValue.getElement("XPATH", "Createschedulebtn")
        ISubject = self.getValue.getInputValue("Createschedule", "ISubject")
        IDescription = self.getValue.getInputValue("Createschedule", "IDescription")
        
        self.driver.find_element_by_xpath(Createschedulelink).click()
        time.sleep(10)
        self.driver.find_element_by_xpath(Subject).send_keys(ISubject)
        self.driver.find_element_by_xpath(Description).send_keys(IDescription)
        self.driver.find_element_by_xpath(Createschedulebtn).click()
        time.sleep(5)
        self.getscreenshotTest.screenshot("Createschedule")
        
        
    def tearDown(self):
        Login.tearDown(self)

    if __name__ == "__main__":
        unittest.main()