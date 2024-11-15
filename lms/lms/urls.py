"""
URL configuration for lms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import (PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,
                                       PasswordResetCompleteView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),

    path('reset_password/', PasswordResetView.as_view(template_name="registration/password-reset.html"),
         name="password_reset"),
    path('reset_password/done/', PasswordResetDoneView.as_view(template_name="registration/password-reset-done.html"),
         name="password_reset_done"),
    path('reset_password/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name="registration/password-reset-confirm.html"),
         name="password_reset_confirm"),
    path('reset_password/complete/',
         PasswordResetCompleteView.as_view(template_name="registration/password-reset-complete.html"),
         name="password_reset_complete"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "LMS Admin"
admin.site.site_title = "LMS Admin Portal"
admin.site.index_title = "Welcome to LMS Portal"

