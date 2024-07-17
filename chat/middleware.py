# chat/middleware.py
from django.contrib.auth import login
from django.utils.deprecation import MiddlewareMixin
from accounts.models import CustomUser
import logging

logger = logging.getLogger(__name__)


class AutoLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            try:
                user = CustomUser.objects.get(username='guy')
                login(request, user)
            except CustomUser.DoesNotExist:
                logger.error('CustomUser with username "guy" does not exist.')
        response = self.get_response(request)
        return response


class SomeMiddleware(MiddlewareMixin):
    def __call__(self, request):
        username = 'guy'
        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            user = None
            logger.error(f'CustomUser with username "{username}" does not exist.')
        request.user = user
        response = self.get_response(request)
        return response
