# from django.contrib import messages
from .models import Notification
from .forms import PrivateMessageForm
from .models import PrivateMessage
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView, CreateView

from .forms import ArticleForm, CommentForm
from .models import Article, Comment

User = get_user_model()


def page_404_test(request):
    response = render(request, 'chat/page_404.html', {})
    response.status_code = 404
    return response


def custom_404(request, exception):
    return render(request, '404.html', {}, status=404)


def Index(request):
    return render(request, 'chat/index.html')


def signup(request):
    return render(request, 'chat/../accounts/templates/accounts/signup.html')


class ArticleListView(ListView):
    model = Article
    template_name = 'chat/article_list.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        return Article.objects.select_related('author').all()


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'chat/article_detail.html'
    context_object_name = 'article'

    def get_queryset(self):
        return Article.objects.select_related('author').prefetch_related('comments')

    def get_object(self, queryset=None):
        try:
            obj = super().get_object(queryset)
            return obj
        except Article.DoesNotExist:
            print("Lin 41 views.py - Article does not exist!")  # Ajouter cette ligne pour le débogage
            raise Http404("No Article matches the given query.")

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
        response = super().form_valid(form)
        followers = self.request.user.followers.all()
        for follower in followers:
            Notification.objects.create(
                recipient=follower,
                message=f'{self.request.user.username} a publié un nouvel article : "{self.object.title}".'
            )
        return response


@login_required
def article_like(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user.is_authenticated:
        if request.user in article.likes.all():
            article.likes.remove(request.user)
        else:
            article.likes.add(request.user)
    return redirect('chat:article_detail', pk=pk)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'chat/comment_form.html'

    def form_valid(self, form):
        form.instance.article = get_object_or_404(Article, pk=self.kwargs['pk'])
        form.instance.author = self.request.user
        response = super().form_valid(form)
        Notification.objects.create(
            recipient=self.object.article.author,
            message=f'New comment on your article "{self.object.article.title}" by {self.request.user.username}'
        )
        if form.instance.parent:
            Notification.objects.create(
                recipient=form.instance.parent.author,
                message=f'{self.request.user.username} a répondu à votre commentaire.'
            )
        return response

    def get_success_url(self):
        article_id = self.object.article.pk
        return reverse('chat:article_detail', kwargs={'pk': article_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_id = self.kwargs.get('pk')
        context['article'] = get_object_or_404(Article.objects.select_related('author'), pk=article_id)
        return context


@login_required
@require_POST
def add_comment(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.author = request.user  # Assurez-vous si l'utilisateur est authentifié
        comment.save()
    return redirect('chat:article_detail', pk=article.pk)


@login_required
def inbox(request):
    messages = PrivateMessage.objects.filter(recipient=request.user).order_by('-timestamp')
    return render(request, 'chat/inbox.html', {'messages': messages})


@login_required
def send_message(request):
    if request.method == 'POST':
        form = PrivateMessageForm(request.POST)
        if form.is_valid():
            private_message = form.save(commit=False)
            private_message.sender = request.user
            private_message.save()
            return redirect('chat:inbox')
    else:
        form = PrivateMessageForm()
    return render(request, 'chat/send_message.html', {'form': form})


@login_required
def notifications(request):
    user_notifications = Notification.objects.filter(recipient=request.user, is_read=False)
    return render(request, 'chat/notifications.html', {'notifications': user_notifications})


@login_required
def mark_notification_as_read(request, notification_id):
    notification = get_object_or_404(Notification, pk=notification_id, recipient=request.user)
    notification.is_read = True
    notification.save()
    return redirect('chat:notifications')


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            user.last_ip = get_client_ip(request)
            user.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/../accounts/templates/accounts/login.html', {'form': form})


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
