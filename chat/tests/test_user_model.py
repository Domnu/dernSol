from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTest(TestCase):
    def test_create_custom_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='testuser', password='password')
        self.assertEqual(user.username, 'testuser')
