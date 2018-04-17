
import time
import unittest
from selenium import webdriver
from hpeu.Tools.ReadFile import ReadFile
from hpeu.Tools.GetScreenshot import GetScreenshot


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.getValue=ReadFile()
        self.getScreenTest = GetScreenshot(self.driver)
    def test_LoginTest(self):
        mydriver = self.driver
        myURL = self.getValue.getURL("newtoursSystem","SystemURL" )
        mydriver.get(myURL)
        time.sleep(3)
        userName = self.getValue.getElement('XPATH',"UsernameInputBox")
        password = self.getValue.getElement('XPATH',"PasswordInputBox")
        loginbtn = self.getValue.getElement('XPATH',"LoginBtn")
        Inputname = self.getValue.getInputValue("Login","name")
        Inputpassword = self.getValue.getInputValue("Login","password")
        mydriver.find_element_by_xpath(userName).send_keys(Inputname)
        mydriver.find_element_by_xpath(password).send_keys(Inputpassword)
        mydriver.find_element_by_xpath(loginbtn).click()
        time.sleep(25)
        
        check1 = self.getValue.getExistElement("CheckPointXpath","CheckPoint_SIGN")
        check2 = self.getValue.getExistElement( "CheckPointXpath","CheckPoint_Filght")
        check1Exist = self.getValue.getExistElement("LoignChenckPoint", "ChenckElement1")
        check2Exist = self.getValue.getExistElement("LoignChenckPoint", "ChenckElement2")
        self.assertEqual(mydriver.find_element_by_xpath(check1).text,check1Exist)
        self.assertEqual(mydriver.find_element_by_xpath(check2).text, check2Exist)
        self.getScreenTest.screenshot("Login")
    def tearDown(self):
        self.driver.close()

       
    if __name__ == '__main__':
        unittest.main()
    
    
    