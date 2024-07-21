from django.test import TestCase
from django.urls import reverse
from ..models import Article, Comment
from django.contrib.auth import get_user_model

User = get_user_model()


class ArticleIntegrationTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

    def test_create_article_and_comment(self):
        # Create Article
        response = self.client.post(reverse('chat:article_create'), {
            'title': 'Test Article',
            'body': 'Test content'
        })
        self.assertEqual(response.status_code, 302)
        article = Article.objects.get(title='Test Article')
        self.assertEqual(article.body, 'Test content')

        # Create Comment
        response = self.client.post(reverse('chat:comment_create', kwargs={'pk': article.pk}), {
            'body': 'Test comment'
        })
        self.assertEqual(response.status_code, 302)
        comment = Comment.objects.get(body='Test comment')
        self.assertEqual(comment.article, article)
        self.assertEqual(comment.author, self.user)
