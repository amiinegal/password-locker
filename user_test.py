
import unittest
from user import User
from credentials import Credentials

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user and credentials class behaviours.
    Args: 
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Setup method to run before each test case
        '''
        self.new_user = User("amiin", "egal", "amiinegal", "12345")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,"amiin")
        self.assertEqual(self.new_user.last_name,"egal")
        self.assertEqual(self.new_user.user_name, "amiinegal")
        self.assertEqual(self.new_user.password, "12345")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        ''' 
        User.user_list = []
    
    def test_save_user(self):
        '''
        test_save_user test case to test if a new user is saved into the user_list
        '''
        self.new_user.save_user()
        self. assertEqual(len(User.user_list),1)    

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Test","user","12345","test@user.com")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("adan","ali","manka","8888")
        test_user.save_user()
        self.new_user.delete_user()    
        self.assertEqual(len(User.user_list),1)

    def test_find_user_by_user_name(self):
        '''
        Test to check if we can find a user by their username and display their details"
        '''
        self.new_user.save_user()
        test_user = User("abdi", "yusuf", "abdi", "ngeshy")
        test_user.save_user()

        find_user = User.find_by_user_name("abdi")

        self.assertEqual(find_user.password, test_user.password)
    def test_user_exists(self):
        '''
        test to check if we can return a boolean if we can not find the user.
        '''
        self.new_user.save_user()
        test_user = User("khalo","nana","khalid","rkelly")
        test_user.save_user()

        user_exists = User.user_exist("khalid")
        self.assertTrue(user_exists)   

if __name__ == '__main__':
    unittest.main()    