from django.contrib.auth import get_user_model
from django.test import TestCase


class UserAccountTests(TestCase):
    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser("testuser", "password")
        self.assertEqual(super_user.username, "testuser")
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)

        self.assertEqual(str(super_user), "testuser")

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                username="username1",
                password="password",
                is_superuser=False,
            )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                username="username1",
                password="password",
                is_staff=False,
            )

    def test_new_user(self):
        db = get_user_model()
        user = db.objects.create_user("testuser", "password")
        self.assertEqual(user.username, "testuser")
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)

        with self.assertRaises(ValueError):
            db.objects.create_user(
                username="",
                password="password",
            )
