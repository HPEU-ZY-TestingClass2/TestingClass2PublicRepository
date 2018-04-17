# coding=utf-8
'''
Created on 2018��4��12��

@author: wangz
'''
import unittest
from selenium import webdriver


class LoginTest(unittest.TestCase):


    def setUp(self):
        self.mydriver = webdriver.Firefox()
        self.mydriver.get('http://192.168.1.19/ciircrm/index.php?&m=user&a=login')





    def test_login(self):
        wzdriver = self.mydriver
        wzdriver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/form/fieldset/input[1]').send_keys('admin')
        wzdriver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/form/fieldset/input[2]').send_keys('admin')
        wzdriver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/form/fieldset/input[3]').click()
    def tearDown(self):
        self.mydriver.close()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()