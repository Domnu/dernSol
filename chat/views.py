from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView, CreateView

from .forms import ArticleForm, CommentForm
from .models import Article, Comment


class BaseView(LoginRequiredMixin):
    model = Article
    template_name = None


def Index(request):
    return render(request, 'chat/index.html')


def signup(request):
    return render(request, 'chat/signup.html')


class ArticleListView(BaseView, ListView):
    template_name = 'chat/article_list.html'


class ArticleDetailView(BaseView, DetailView):
    template_name = 'chat/article_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(
            article=self.object)
        return context


class ArticleCreateView(BaseView, CreateView):
    form_class = ArticleForm
    template_name = 'chat/article_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'chat/comment_form.html'  # Ensure this template exists and is correct

    # success_url no longer needed as get_success_url is used instead
    # success_url n'est plus nécessaire car get_success_url est utilisé à la place
    # success_url = reverse_lazy('chat:article_list')  # Remplace 'chat:article_list' par l'URL de redirection souhaitée

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author of the comment to the current user
        form.instance.article = Article.objects.get(
            pk=self.kwargs['pk'])  # Assuming you pass the article's PK in the URL
        return super().form_valid(form)  # Save the form and the instance

    def get_success_url(self):
        article_id = self.object.article.pk  # Get the article ID of the newly created comment
        return reverse('chat:article_detail', kwargs={'pk': article_id})  # Use reverse and not reverse_lazy here

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Assure-toi que l'ID est passé correctement et que l'article existe.
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