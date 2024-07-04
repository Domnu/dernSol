from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['title', 'body']
        error_messages = {
            'title': {
                'required': "Ce champ est obligatoire",
            },
            'body': {
                'required': "Ce champ est obligatoire",
            },
        }

