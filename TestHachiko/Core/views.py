from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from Core.customToken import IsTelegramUser
from Core.serializers import RegisterUserSerializer
from .models import AppUsers
from rest_framework.response import Response
import requests
from TestHachiko.settings import API_CHECK_KEY

class UserExsistAPIVIew(APIView):
    """
    Предварительная проверка, зарегистрирован ли уже пользователь (для оптимизации)
    """
    permission_classes = [AllowAny]
    def get(self, request, user_id=None):
        try:
            if AppUsers.objects.filter(telegram_id=user_id).exists():
                return Response("OK")
            else:
                return Response("NOT_FOUND")
        except Exception as e:
            return Response(str(e), status=500)

class RegisterUsersAPIView(APIView):
    """
    Регистрация пользователя ботом telegram
    """
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            serializer = RegisterUserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except Exception as e:
            return Response(str(e), status=500)


class CheckIMEIAPIView(APIView):
    """
      запрос на проверку IMEI, интеграция со сторонним сервисом
    """
    permission_classes = [IsTelegramUser]
    def post(self, request):
        try:
            imei = request.data.get('imei')
            if not imei:
                return Response({"error": "IMEI is required"}, status=400)

            url = "https://api.imeicheck.net/v1/checks"
            headers = {
                "Authorization": f"Bearer {API_CHECK_KEY}",
                "Accept-Language": "en"
            }
            payload = {"deviceId": imei, "serviceId": 1}

            response = requests.post(url, json=payload, headers=headers)

            if response.status_code == 200:
                return Response(response.json(), status=200)
            else:
                return Response({
                    "details": response.json()
                }, status=response.status_code)

        except requests.exceptions.RequestException as e:
            return Response({"error": "Сетевая ошибка", "details": str(e)}, status=500)
        except Exception as e:
            return Response({"error": "Произошла ошибка", "details": str(e)}, status=500)