from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView, CreateView

from .forms import ArticleForm, CommentForm
from .models import Article, Comment


def custom_page_not_found(request, exception):
    return render(request, 'chat/404.html', status=404)


def Index(request):
    return render(request, 'chat/index.html')


def signup(request):
    return render(request, 'chat/signup.html')


class ArticleListView(ListView):
    model = Article
    template_name = 'chat/article_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'chat/article_detail.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj:
            raise Http404("Article not found")
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(article=self.object)
        return context


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
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


@require_POST
def add_comment(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.author = request.user
        comment.save()
    return redirect('chat:article_detail', pk=article.pk)
