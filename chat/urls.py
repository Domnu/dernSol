from django.urls import path
from .views import Index, signup, ArticleListView, ArticleDetailView, ArticleCreateView, CommentCreateView, \
    add_comment

app_name = 'chat'

urlpatterns = [
    path('', Index, name='index'),
    path('signup/', signup, name='signup'),
    path('article_list/', ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('article/<int:pk>/comment/create/', CommentCreateView.as_view(), name='comment_create'),
    path('article/<int:pk>/add_comment/', add_comment, name='add_comment'),  # Ajoutez cette ligne
]