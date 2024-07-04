from django.contrib.auth.models import User
from django.test import TestCase


class MyTest(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username='guy', password='yugyugyug')

    def test_something(self):
        # Votre code de test ici
        pass

