from collections import UserList
from django.urls import path, include

from .views import LoginView, RefreshView, logout_view, MeApiView, UserCreateForApparatAPIView, UserCreateForDirektorAPIView, GroupListAPIView, UserListAPIView, UserDeleteAPIView, MonitoringUserCreateAPIView, UserUpdateForApparatAPIView
urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('me/', MeApiView.as_view(), name="me"),
    path('token-refresh/', RefreshView.as_view(), name="token_refresh"),
    path('logout/', logout_view, name="logout"),
    path('userCreateForApparat/', UserCreateForApparatAPIView.as_view(), name="user-create-for-apparat"),
    path('userUpdateForApparat/<pk>/', UserUpdateForApparatAPIView.as_view(), name="user-update-for-apparat"),
    path('userCreateForDirektor/', UserCreateForDirektorAPIView.as_view(), name="user-create-for-direktor"),
    path('monitoring_user_create/', MonitoringUserCreateAPIView.as_view(), name="monitoring_user_create"),
    path('groups/', GroupListAPIView.as_view(), name="group-list"),
    path('users/', UserListAPIView.as_view(), name="user-list"),
    path('users/<pk>', UserDeleteAPIView.as_view(), name="user-delete"),
]
