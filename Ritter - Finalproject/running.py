import unittest 
from login import TestLogin
 
 
if __name__ == "__main__": 
    suite = unittest.TestSuite() 
    suite.addTest(TestLogin('test_a_success_login'))
    suite.addTest(TestLogin('test_username_password_invalid'))
    suite.addTest(TestLogin('test_All_blank'))
    suite.addTest(TestLogin('test_forgot_password'))
    suite.addTest(TestLogin('test_Logout'))

runner = unittest.TextTestRunner() 
runner.run(suite)
