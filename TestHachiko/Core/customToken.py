from rest_framework.permissions import BasePermission
from Core.models import AppUsers
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
import logging

logger = logging.getLogger('django')
class IsTelegramUser(BasePermission):
    """
    Custom permission to check if the request comes from a Telegram user with a valid token.
    """
    def has_permission(self, request, view):
        auth_header = request.headers.get('Authorization')

        if auth_header is None:
            # logger.warning("Попытка доступа без токена авторизации.")
            return False
        try:
            # Предположим, что токен передается как Bearer <token>
            token_type, token = auth_header.split()

            if token_type != 'Bearer':
                # logger.warning(f"Некорректный тип токена: {token_type}")
                return False
                # Проверяем, существует ли пользователь с таким токеном
            is_valid_user = AppUsers.objects.filter(token=token).exists()
            # if not is_valid_user:
                # logger.warning(f"Токен не найден в базе данных: {token}")
            return is_valid_user

        except (ValueError, AppUsers.DoesNotExist):
            # logger.error("Ошибка разбора заголовка авторизации.")
            return False




class TelegramTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            # logger.warning("Запрос без заголовка Authorization.")
            return None  # Если токен отсутствует, пропускаем аутентификацию
        try:
            token_type, token = auth_header.split()
            if token_type != 'Bearer':
                # logger.warning(f"Неверный тип токена: {token_type}. Ожидается 'Bearer'.")
                raise AuthenticationFailed('Invalid token type')
            try:
                # Находим пользователя по токену
                user = AppUsers.objects.get(token=token)
                return (user, None)
            except AppUsers.DoesNotExist:
                # logger.error(f"Попытка аутентификации с несуществующим токеном: {token}")
                raise AuthenticationFailed('Invalid token or user not found')
        except ValueError:
            # logger.error("Ошибка формата заголовка авторизации.")
            raise AuthenticationFailed('Invalid token header')
        return None
