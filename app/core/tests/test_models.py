from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):


    def test_create_user_with_email_successful(self):
        """test creating a new user with an email is successfull"""
        email="thisistest@myemail.com"
        password="thispass123!"
        user=get_user_model().objects.create_user(
            email= email,
            password= password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalized(self):
        """test the email for a new user is normalized"""
        email='thisistest@MYEMAIL.COM'
        user=get_user_model().objects.create_user(email, 'thispass123!')

        self.assertEqual(user.email, email.lower())


    def test_new_user_invalid_email(self):
        """Test Creating user with no email will raise error"""
        with self.assertRaises(ValueError):
          get_user_model().objects.create_user(None, 'thispass123!')


    def test_create_new_superuser(self):
        """test create a new superuser"""
        user = get_user_model().objects.create_superuser(
          'thisistest@myemail.com',
          'thispass123!'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)


