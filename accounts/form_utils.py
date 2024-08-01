# accounts/form_utils.py

from django.contrib import messages
from django.shortcuts import redirect


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
