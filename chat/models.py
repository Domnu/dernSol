from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User, Group, Permission

from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True, default='default_username')
    password = models.CharField(max_length=128, default='default_password')
    # Ajoutez un related_name unique pour le champ groups
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='myuser_set',  # Changer 'user_set' en 'myuser_set'
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    # Ajoutez un related_name unique pour le champ user_permissions
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='myuser_permissions_set',  # Changer 'user_set' en 'myuser_permissions_set'
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, null=True)  # Titre facultatif
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('chat:article_detail', kwargs={'pk': self.article.pk})


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'article')
