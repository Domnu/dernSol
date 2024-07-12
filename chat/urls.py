from django.urls import path
from .views import Index, signup, ArticleListView, ArticleDetailView, ArticleCreateView, CommentCreateView, add_comment, custom_404

app_name = 'chat'

urlpatterns = [
    path('', Index, name='index'),
    path('signup/', signup, name='signup'),
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('articles/create/', ArticleCreateView.as_view(), name='article_create'),
    path('articles/<int:pk>/comment/', CommentCreateView.as_view(), name='comment_create'),
    path('articles/<int:pk>/add_comment/', add_comment, name='add_comment'),
]

handler404 = 'chat.views.custom_404'
