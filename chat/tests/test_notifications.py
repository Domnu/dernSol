from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from chat.models import Article, Comment, Notification

User = get_user_model()


class NotificationTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.follower = User.objects.create_user(username='follower', password='password')
        self.user.followers.add(self.follower)
        self.client.login(username='testuser', password='password')

    def test_article_creation_notification(self):
        response = self.client.post(reverse('chat:article_create'), {
            'title': 'Test Article',
            'body': 'Test content'
        })
        self.assertEqual(response.status_code, 302)
        notification = Notification.objects.get(recipient=self.follower)
        self.assertEqual(notification.message, 'testuser a publié un nouvel article : "Test Article".')

    def test_mark_notification_as_read(self):
        notification = Notification.objects.create(recipient=self.user, message='Test notification')
        self.client.get(reverse('chat:mark_notification_as_read', args=[notification.id]))
        notification.refresh_from_db()
        self.assertTrue(notification.is_read)
