from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class MyTest(TestCase):

    def setUp(self):
        self.test_user = User.objects.create_user(username='guy', password='yugyugyug')

    def test_something(self):
        self.assertEqual(self.test_user.username, 'guy')
