from rest_framework import routers, urlpatterns
from django.urls import path, include
from . import views

router = routers.DefaultRouter()

router.register('', viewset=views.NotificationViewset, basename='Notification')

urlpatterns = [
    path('donation/notification/', views.DonationNotificationListAPIView.as_view()),
    path('donation/complete/<pk>/',
         views.DonationNotificationDetailAPIView.as_view()),
    path('', include(router.urls)),
]
