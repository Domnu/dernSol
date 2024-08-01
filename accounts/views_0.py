# accounts/views.py

from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render

from .forms import SignupForm
from .models import CustomUser
from .utils import generate_unique_username
from .form_utils import process_form, handle_form_errors


def test_message_view(request):
    messages.add_message(request, messages.INFO, 'Ceci est un message test')
    return render(request, 'chat/base_generic.html')


def check_username(request):
    username = request.GET.get('username', None)
    if CustomUser.objects.filter(username=username).exists():
        unique_username = generate_unique_username(username)
        return JsonResponse({'exists': True, 'suggested_username': unique_username})
    return JsonResponse({'exists': False})


def signup(request):
    response = process_form(request, SignupForm, "Inscription réussie !", 'chat:index')
    if isinstance(response, HttpResponseRedirect):
        return response
    return render(request, 'accounts/signup.html', {'form': response})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, 'Connexion réussie.')
            return redirect('chat:article_create')
        else:
            handle_form_errors(request, form)
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
