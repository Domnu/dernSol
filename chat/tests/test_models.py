from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Article, Comment

User = get_user_model()


class ArticleModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.article = Article.objects.create(
            author=self.user,
            title="Test Article",
            body="This is a test article."
        )

    def test_article_creation(self):
        self.assertEqual(self.article.title, "Test Article")
        self.assertEqual(self.article.author.username, 'testuser')
        self.assertEqual(str(self.article), "Test Article")

    def test_article_absolute_url(self):
        self.assertEqual(self.article.get_absolute_url(), f'/articles/{self.article.pk}/')

    def test_article_total_likes(self):
        self.article.likes.add(self.user)
        self.assertEqual(self.article.total_likes(), 1)


class CommentModelTest(TestCase):

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

    def test_comment_creation(self):
        self.assertEqual(self.comment.body, "This is a test comment.")
        self.assertEqual(self.comment.author.username, 'testuser')
        self.assertEqual(str(self.comment), f'Comment by {self.user} on {self.article}')

    def test_comment_has_replies(self):
        self.assertFalse(self.comment.has_replies())

    def test_comment_total_replies(self):
        self.assertEqual(self.comment.total_replies(), 0)
