"""
URL configuration for Agrohub project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users.setup_view import setup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__setup__/', setup_view, name='setup'),  # One-time setup URL
    path('', include('marketplace.urls')),
    path('users/', include('users.urls')),
    path('chatbot/', include('chatbot.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
