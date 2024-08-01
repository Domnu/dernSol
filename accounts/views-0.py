# accounts/views.py
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import SignupForm


def test_message_view(request):
    messages.add_message(request, messages.INFO, 'Ceci est un message test')
    return render(request, 'chat/base_generic.html')


def handle_form_errors(request, form):
    for field, errors in form.errors.items():
        for error in errors:
            messages.error(request, f"{error}")


def process_form(request, form_class, success_message, redirect_url):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, success_message)
            return redirect(redirect_url)
        else:
            handle_form_errors(request, form)
    else:
        form = form_class()
    return form


def signup(request):
    form = process_form(request, SignupForm, "Utilisateur créé avec succès.", 'chat:index')
    return render(request, 'accounts/signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, 'Connexion réussie.')
            return redirect('chat:inbox')
        else:
            handle_form_errors(request, form)
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
