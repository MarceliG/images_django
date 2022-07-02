from django.test import SimpleTestCase
from django.urls import reverse, resolve
from members.views import login_user, logout_user


class TestUrls(SimpleTestCase):
    def test_login_url_resolved(self):
        url = reverse("login")
        self.assertEquals(resolve(url).func, login_user)

    def test_logout_url_resolved(self):
        url = reverse("logout")
        self.assertEquals(resolve(url).func, logout_user)
