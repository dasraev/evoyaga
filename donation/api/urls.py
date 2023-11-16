from rest_framework import routers
from . import views
from django.urls.conf import include, path

router = routers.DefaultRouter()

router.register('donations', viewset=views.DonationViewset, basename='Donation')

urlpatterns = [
    path('', include(router.urls)),
]