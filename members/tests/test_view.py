from django.test import Client, SimpleTestCase
from django.urls import reverse


class BaseTest(SimpleTestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse("login")
        self.logout_url = reverse("logout")
        self.user = {
            "email": "testemail@gmail.com",
            "username": "test",
            "password": "test",
            "password2": "test",
            "name": "fullname",
        }

        return super().setUp()


class LoginTest(BaseTest):
    def test_login_user_not_POST(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "authenticate/login.html")


# TODO
# check correctly login and logout.
