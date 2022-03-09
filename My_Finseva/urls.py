"""My_Finseva URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from main.views import home_view, pricing_view, services_view, privacy_policy_view, refund_policy_view, t_and_c_view, contact_view
from accounts.views import auth_view, logout_view, verify_email_view
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home_page'),
    path('contact/', contact_view, name='contact_page'),
    path('pricing/', pricing_view, name='pricing_page'),
    path('services/', services_view, name='services_page'),
    path('privacy-policy/', privacy_policy_view, name='privacy_policy_page'),
    path('refund-policy/', refund_policy_view, name='refund_policy_page'),
    path('terms&conditions/', t_and_c_view, name='t_and_c_page'),
    path('login/', auth_view, name='auth_page'),
    path('logout/', logout_view, name='logout_page'),
    path('verify_email/<uidb64>/<token>', verify_email_view, name='verify_email'),
    path('reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset/', PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password-reset-complete/', PasswordResetView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('reset-complete/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('admin-one/', include('admin_one.urls')),
]