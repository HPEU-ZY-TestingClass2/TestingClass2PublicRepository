import unittest
import time
from selenium import webdriver
from hpeu.Tools.ReadFile import ReadFile
from hpeu.CRM.Login import Login
from hpeu.Tools.GetScreenshot import GetScreenshot
class Createtask(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.getValue = ReadFile()
        self.getscreenshotTest = GetScreenshot(self.driver)
    def test_Createtask(self):
        Login.test_Login(self)
        time.sleep(5)
        
        Createtasklink = self.getValue.getElement("XPATH", "Createtasklink")
        TaskSubject = self.getValue.getElement("XPATH", "TaskSubject")
        Tasker = self.getValue.getElement("XPATH", "Tasker")
        TaskDescription = self.getValue.getElement("XPATH", "TaskDescription")
        ITaskSubject = self.getValue.getInputValue("CreateTask", "ITaskSubject")
        ITaskDescription = self.getValue.getInputValue("CreateTask", "ITaskDescription")
        ITasker = self.getValue.getInputValue("CreateTask", "ITasker")
        Createtaskbtn = self.getValue.getElement("XPATH", "Createtaskbtn")
        
        self.driver.find_element_by_xpath(Createtasklink).click()
        self.driver.find_element_by_xpath(TaskSubject).send_keys(ITaskSubject)
        self.driver.find_element_by_xpath(Tasker).send_keys(ITasker)
        self.driver.find_element_by_xpath(TaskDescription).send_keys(ITaskDescription)
        self.driver.find_element_by_xpath(Createtaskbtn).click()
        time.sleep(5)
        self.getscreenshotTest.screenshot("Createtask")
        
    def tearDown(self):
        Login.tearDown(self)

    if __name__ == "__main__":
        unittest.main()