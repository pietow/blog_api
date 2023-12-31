"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include # new
from allauth.account.views import ConfirmEmailView # new
from django.views.generic import TemplateView # new


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')), # new
    path('api-auth/', include('rest_framework.urls')), # new
    # path('api/v1/dj-rest-auth/', include('django.contrib.auth.urls')), # new
    path('api/v1/dj-rest-auth/registration/account-confirm-email/<str:key>/',
         TemplateView.as_view(template_name='email_confirmation.html'),
         name='account_confirm_email'),
    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')), # new
    # path('api/v1/dj-rest-auth/account-confirm-email/<str:key>', ConfirmEmailView.as_view(), name='account_email_verification_sent'), # new
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')), # new
]
