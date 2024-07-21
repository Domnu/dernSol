from django.test import TestCase
from ..forms import ArticleForm, CommentForm
from ..models import Article, Comment
from django.contrib.auth import get_user_model

User = get_user_model()


class ArticleFormTest(TestCase):

    def test_valid_form(self):
        user = User.objects.create_user(username='testuser', password='password')
        data = {'author': user.id, 'title': 'Test Article', 'body': 'Test content'}
        form = ArticleForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'title': '', 'body': 'Test content'}
        form = ArticleForm(data=data)
        self.assertFalse(form.is_valid())


class CommentFormTest(TestCase):

    def test_valid_form(self):
        user = User.objects.create_user(username='testuser', password='password')
        article = Article.objects.create(author=user, title='Test Article', body='Test content')
        data = {'article': article.id, 'author': user.id, 'body': 'Test comment'}
        form = CommentForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'body': ''}
        form = CommentForm(data=data)
        self.assertFalse(form.is_valid())
