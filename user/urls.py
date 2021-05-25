from django.urls import path, include
from .views import UserCreateView, UserCreateDoneTV, UserCreateView
from django.contrib import admin

app_name = 'user'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    # 회원 가입 및 처리
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(),name='register_done'),
]