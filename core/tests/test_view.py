from django.contrib.auth import get_user_model
from core.tests.test_setup import TestSetUp

User = get_user_model()


class TestView(TestSetUp):

    def test_user_cannot_register(self):
        response = self.client.post(self.register_url)
        import pdb
        pdb.set_trace()
        self.assertEquals(response.status_code, 400)

    def test_user_register(self):
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.data['email'], self.user_data['email'])
        self.assertEqual(response.data['username'], self.user_data['username'])
        self.assertEquals(response.status_code, 201)

    def test_user_cannot_login_with_unverified_email(self):
        self.client.post(self.register_url, self.user_data, format="json")
        response = self.client.post(self.login_url, self.user_data, format="json")
        self.assertEqual(response.status_code, 401)

    def test_user_can_login_after_verification(self):
        response = self.client.post(self.register_url, self.user_data, format="json")
        email = response.data['email']
        user = User.objects.get(email=email)
        user.is_verified = True
        user.save()
        response = self.client.post(self.login_url, self.user_data, format="json")
        self.assertEqual(response.status_code, 200)
