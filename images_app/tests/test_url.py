from django.test import SimpleTestCase
from django.urls import reverse, resolve
from images_app.views import home


class TestUrls(SimpleTestCase):
    def test_home_url_resolved(self):
        url = reverse("home")
        self.assertEquals(resolve(url).func, home)
