from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .yasg import urlpatterns as doc_urls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.views.generic import TemplateView
from .views import index
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),

    path('auth/', include('accounts.api.urls')),

    path('api/notifications/', include('notification.api.urls'), name='notifications'),
    path('api/info/', include('info.api.urls'), name='regions'),
    path('api/juvenile/', include('juvenile.api.urls'), name='juveniles'),
    path('api/', include('donation.api.urls'), name='donations'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += doc_urls
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)