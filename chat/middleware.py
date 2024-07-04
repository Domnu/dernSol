from django.contrib.auth import login
from django.utils.deprecation import MiddlewareMixin
from chat.models import MyUser
import logging

logger = logging.getLogger(__name__)

class AutoLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            try:
                # Remplacez 'guy' par le nom d'utilisateur que vous souhaitez utiliser
                user = MyUser.objects.get(username='guy')
                login(request, user)
            except MyUser.DoesNotExist:
                logger.error('MyUser with username "guy" does not exist.')
                # Vous pouvez ajouter une logique pour gérer le cas où l'utilisateur n'existe pas
        response = self.get_response(request)
        return response


class SomeMiddleware(MiddlewareMixin):
    def __call__(self, request):
        username = 'guy'  # Remplacez par la logique pour obtenir le nom d'utilisateur
        try:
            user = MyUser.objects.get(username=username)
        except MyUser.DoesNotExist:
            user = None
            logger.error(f'MyUser with username "{username}" does not exist.')
            # Ajoutez une logique pour gérer le cas où l'utilisateur n'existe pas
        request.user = user
        response = self.get_response(request)
        return response
