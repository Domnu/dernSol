from django.urls import path
from .views import Index, ArticleListView, ArticleDetailView, ArticleCreateView, CommentCreateView, article_like, inbox, send_message, notifications, mark_notification_as_read

app_name = 'chat'

urlpatterns = [
    path('', Index, name='index'),
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('articles/new/', ArticleCreateView.as_view(), name='article_create'),
    path('articles/<int:pk>/like/', article_like, name='article_like'),
    path('articles/<int:pk>/comment/', CommentCreateView.as_view(), name='comment_create'),
    path('inbox/', inbox, name='inbox'),
    path('send-message/', send_message, name='send_message'),
    path('notifications/', notifications, name='notifications'),
    path('notifications/mark-as-read/<int:notification_id>/', mark_notification_as_read, name='mark_notification_as_read'),
]
