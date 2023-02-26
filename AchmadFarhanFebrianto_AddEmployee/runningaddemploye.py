import unittest 
from Addemployee import TestAddemployee
 
 
if __name__ == "__main__": 
    suite = unittest.TestSuite() 
    suite.addTest(TestAddemployee('test_positive_add_employee'))
    suite.addTest(TestAddemployee('test_negative_add_employee'))
    suite.addTest(TestAddemployee('test_positive_add_employee_login_detail'))
    suite.addTest(TestAddemployee('test_negative_add_employee_login_detail'))


runner = unittest.TextTestRunner() 
runner.run(suite)