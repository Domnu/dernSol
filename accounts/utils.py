# accounts/utils.py

from django.utils.text import slugify
from .models import CustomUser


def generate_unique_username(base_username):
    """
    Génère un nom d'utilisateur unique en ajoutant une chaîne aléatoire si le nom d'utilisateur existe déjà.
    """
    base_username = slugify(base_username)
    username = base_username
    counter = 1
    while CustomUser.objects.filter(username=username).exists():
        username = f"{base_username}{counter}"
        counter += 1
    return username
