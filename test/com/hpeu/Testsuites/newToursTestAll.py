import unittest
import os
import sys
sys.path.append(os.path.split(os.path.split(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0])[0])[0])

from hpeu.newTours.Login import LoginTest
from hpeu.newTours.Search import SearchTest
from hpeu.newTours.Order import OrderTest




if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(LoginTest("test_LoginTest"))
    suite.addTest(SearchTest("test_SearchTest"))
    suite.addTest(OrderTest("test_OrderTest"))
    
   
    Runner = unittest.TextTestRunner()
    
    Runner.run(suite)