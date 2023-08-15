from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker


class TestSetUp(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')  # Assuming you have a URL named 'register' in your app's URLs
        self.login_url = reverse('login')  # Assuming you have a URL named 'login' in your app's URLs
        self.fake = Faker()

        # Prepare data for user registration
        self.user_data = {
            'email': self.fake.email(),
            'username': self.fake.user_name(),  # Using a more appropriate faker method
            'password': self.fake.password(),  # Using a random password
        }

        super().setUp()  # Call the base class's setUp method

    def tearDown(self):
        super().tearDown()  # Call the base class's tearDown method
