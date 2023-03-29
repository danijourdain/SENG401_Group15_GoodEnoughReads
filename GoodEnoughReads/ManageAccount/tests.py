from django.test import TestCase

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import reverse
# import pymysql

# Create your tests here.

# Run the tests with python manage.py test
# If told that ger doesn't have permission to create a database, run in mysql terminal:
# GRANT ALL PRIVILEGES ON test_ger_db.* TO 'ger'@'localhost';
# I've added into settings.py in GER the name and credenitals for the test database 
# Current error: django.db.utils.ProgrammingError: (1146, "Table 'test_ger_db.user' doesn't exist")

# class SignUpTestCase(TestCase):
#     def setUp(self) -> None:
#         self.validemail = "test@testing.test"
#         self.validfname = "test"
#         self.validlname = "tests"
#         self.validusername = "testUser"
#         self.validpassword = "y"


#     #Test that the signup page exists
#     def test_signup_page_url(self):
#         response = self.client.get("/signup/")
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, template_name='ManageAccount/signup.html')

#     #Test signup with a valid username with valid password
#     def test_signup_form_valid_credentials(self):
#         response = self.client.post(reverse('signup'), data={
#             'email': self.validemail,
#             'fname': self.validfname,
#             'lname': self.validlname,
#             'username': self.validusername,
#             'pw1': self.validpassword,
#             'pw2': self.validpassword
#         })
#         self.assertEqual(response.status_code, 200)
