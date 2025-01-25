from django.urls import path
from .views import RegisterUsersAPIView, UserExsistAPIVIew, CheckIMEIAPIView


urlpatterns = [
    path('register', RegisterUsersAPIView.as_view()),
    path('user-exsist<int:user_id>', UserExsistAPIVIew.as_view()),
    path('check-imei', CheckIMEIAPIView.as_view(), name='check_iemai'),
]