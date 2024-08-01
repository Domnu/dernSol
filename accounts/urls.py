# accounts/urls.py

from django.urls import path
from .views import signup, login, check_username, test_message_view

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
path('check_username/', check_username, name='check_username'),  # Assurez-vous que cette ligne existe
    path('test_message/', test_message_view, name='test_message'),
]