from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from chat.models import Article

User = get_user_model()


class ArticleListViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        Article.objects.create(author=self.user, title="Test Article 1", body="Test content 1")
        Article.objects.create(author=self.user, title="Test Article 2", body="Test content 2")

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/articles/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('chat:article_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('chat:article_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/article_list.html')
