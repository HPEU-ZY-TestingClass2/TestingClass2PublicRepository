import unittest
import time
from hpeu.newTours.Login import LoginTest
from selenium import webdriver
from hpeu.Tools.ReadFile import ReadFile
from hpeu.Tools.GetScreenshot import GetScreenshot
class SearchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.getValue=ReadFile()
        self.getScreenTest = GetScreenshot(self.driver)
    def test_SearchTest(self):
        mydriver = self.driver
        LoginTest.test_LoginTest(self)
        Type1 = self.getValue.getElement("XPATH", "Type1")
        Passengers = self.getValue.getElement("XPATH", "Passengers")
        Depart = self.getValue.getElement("XPATH", "Depart")
        On1 = self.getValue.getElement("XPATH", "On1")
        On2 = self.getValue.getElement("XPATH", "On2")
        Arrive = self.getValue.getElement("XPATH", "Arrive")
        Return1 = self.getValue.getElement("XPATH", "Return1")
        Return2 = self.getValue.getElement("XPATH", "Return2")
        Class_economy = self.getValue.getElement("XPATH", "Class_economy")
        Airline = self.getValue.getElement("XPATH", "Airline")
        ContinueBtn = self.getValue.getElement("XPATH", "ContinueBtn")
        Depart2 = self.getValue.getElement("XPATH", "Depart2")
        Return3 = self.getValue.getElement("XPATH", "Return3")
        ContinueBtn1 = self.getValue.getElement("XPATH", "ContinueBtn1")
        IPassenger = self.getValue.getInputValue("Search", "Passenger")
        IDepart = self.getValue.getInputValue("Search", "Depart")
        IOn1 = self.getValue.getInputValue("Search", "On1")
        IOn2 = self.getValue.getInputValue("Search", "On2")
        IArrive = self.getValue.getInputValue("Search", "Arrive")
        IReturn1 = self.getValue.getInputValue("Search", "Return1")
        IReturn2 = self.getValue.getInputValue("Search", "Return2")
        IAirline = self.getValue.getInputValue("Search", "Airline")
        
        mydriver.find_element_by_xpath(Type1).click()
        mydriver.find_element_by_xpath(Passengers).send_keys(IPassenger)
        mydriver.find_element_by_xpath(Depart).send_keys(IDepart)
        mydriver.find_element_by_xpath(On1).send_keys(IOn1)
        mydriver.find_element_by_xpath(On2).send_keys(IOn2)
        mydriver.find_element_by_xpath(Arrive).send_keys(IArrive)
        mydriver.find_element_by_xpath(Return1).send_keys(IReturn1)
        mydriver.find_element_by_xpath(Return2).send_keys(IReturn2)
        mydriver.find_element_by_xpath(Class_economy).click()
        mydriver.find_element_by_xpath(Airline).send_keys(IAirline)
        time.sleep(5)
        self.getScreenTest.screenshot("Sraerch")
        mydriver.find_element_by_xpath(ContinueBtn).click()
        
        mydriver.find_element_by_xpath(Depart2).click()
        mydriver.find_element_by_xpath(Return3).click()
        mydriver.find_element_by_xpath(ContinueBtn1).click()
        time.sleep(5)
        
        
    def tearDown(self):
        LoginTest.tearDown(self)
    if __name__ == '__main__':
        unittest.main()
    
