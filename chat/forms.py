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
            'body': {
                'required': "Ce champ est obligatoire",
            },
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = False


