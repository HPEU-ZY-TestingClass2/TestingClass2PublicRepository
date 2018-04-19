import unittest
from hpeu.CRM.Login import Login
from hpeu.CRM.CreateClue import CreateClue
from hpeu.CRM.LookClue import LookClue
from hpeu.CRM.CreateCustomer import CreateCustomer
from hpeu.CRM.LookCustomer import LookCustomer
from hpeu.CRM.Createbusiness import Createbusiness
from hpeu.CRM.Lookbusiness import Lookbusiness
from hpeu.CRM.Createschedule import Createschedule
from hpeu.CRM.Lookschedule import Lookschedule
from hpeu.CRM.Createtask import Createtask
from hpeu.CRM.Looktask import Looktask

if __name__ == "__nain__":
    suite = unittest.suite()
    suite.addTest(Login("test_Login"))
    suite.addTest(CreateClue("test_CreateClue"))
    suite.addTest(LookClue("test_LookClue"))
    suite.addTest(CreateCustomer("test_CreateCustomer"))
    suite.addTest(LookCustomer("test_LookCustomer"))
    suite.addTest(Createbusiness("test_Createbusiness"))
    suite.addTest(Lookbusiness("test_Lookbusiness"))
    suite.addTest(Createschedule("test_Createschedule"))
    suite.addTest(Lookschedule("test_Lookschedule"))
    suite.addTest(Createtask("test_Createtask"))
    suite.addTest(Looktask("test_Looktask"))
    
    Runner = unittest.TextTestRunner()
    Runner.run(suite)
    

