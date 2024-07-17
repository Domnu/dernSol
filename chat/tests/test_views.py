# chat/tests/test_views.py

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from chat.models import Article, Comment

User = get_user_model()


class ArticleDetailViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.article = Article.objects.create(
            author=self.user,
            title="Test Article",
            body="This is a test article."
        )

    def test_article_detail_view_404(self):
        invalid_pk = self.article.pk + 1
        response = self.client.get(reverse('chat:article_detail', kwargs={'pk': invalid_pk}))
        self.assertEqual(response.status_code, 404)


class CommentCreateViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.article = Article.objects.create(
            author=self.user,
            title="Test Article",
            body="This is a test article."
        )
        self.comment = Comment.objects.create(
            article=self.article,
            author=self.user,
            body="This is a test comment."
        )

    def test_comment_create_view_404(self):
        self.client.login(username='testuser', password='password')
        invalid_pk = self.article.pk + 1
        response = self.client.post(reverse('chat:comment_create', kwargs={'pk': invalid_pk}), {
            'body': 'This is another test comment.'
        })
        self.assertEqual(response.status_code, 404)
