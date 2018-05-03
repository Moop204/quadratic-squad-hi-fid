from django.test import TestCase
from django.test import Client
from user_profile.models import * 
# Create your tests here.

class LoginTestClass(TestCase):
    client = Client()

    @classmethod
    def setUpTestData(cls):
        
        print("what am I doing")

    def setUp(self):
        self.client = Client()
        pass

    def tearDown(self):
        #Clean up run after every test method.
        pass

    # Asserts that input can be added fine and page loads ok 
    def test_something_that_will_pass(self):
        response = self.client.post('/login/', {'username': 'sample', 'password': 'sample_pass'})
        self.assertEquals(response.status_code, 200)

    def test_something_that_will_fail(self):
        self.assertTrue(True)

    
