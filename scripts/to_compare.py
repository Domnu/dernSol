# accounts/forms.py
from django import forms
from django.contrib.auth import authenticate
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from .utils import generate_unique_username


class CustomAuthenticationForm(forms.Form):
    username = forms.CharField(label='Email ou Nom d\'utilisateur')
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.user_cache = None
        super().__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                try:
                    user_temp = CustomUser.objects.get(email=username)
                    self.user_cache = authenticate(self.request, username=user_temp.username, password=password)
                    if self.user_cache is None:
                        raise forms.ValidationError("Nom d'utilisateur/email ou mot de passe incorrect.")
                except CustomUser.DoesNotExist:
                    raise forms.ValidationError("Nom d'utilisateur/email ou mot de passe incorrect.")
        return self.cleaned_data

    def get_user(self):
        return self.user_cache


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            unique_username = generate_unique_username(username)
            raise forms.ValidationError(
                f"Ce nom / pseudo existe déjà. Nous vous suggérons {unique_username}."
            )
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Cet email existe déjà.")
        return email

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = generate_unique_username(self.cleaned_data['username'])
        if commit:
            user.save()
        return user
