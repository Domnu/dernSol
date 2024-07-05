# chat/views.py

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


def Index(request):
    return render(request, 'chat/index.html')


def signup(request):
    return render(request, 'chat/signup.html')


class ArticleListView(ListView):
    model = Article
    template_name = 'chat/article_list.html'
    context_object_name = 'article_list'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'chat/article_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(article=self.object)
        return context


class ArticleCreateView(CreateView):
    form_class = ArticleForm
    template_name = 'chat/article_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'chat/comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.article = Article.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        article_id = self.object.article.pk
        return reverse('chat:article_detail', kwargs={'pk': article_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_id = self.kwargs.get('pk')
        context['article'] = get_object_or_404(Article, pk=article_id)
        return context
