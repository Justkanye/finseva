from django.urls import path, include
from .views import admin_one_home_view, admin_one_tables_view, admin_one_profile_view, admin_one_forms_view, admin_one_login_view

urlpatterns = [
    path('', admin_one_home_view, name='admin_one_home'),
    path('tables/', admin_one_tables_view, name='admin_one_tables'),
    path('profile/', admin_one_profile_view, name='admin_one_profile'),
    path('forms/', admin_one_forms_view, name='admin_one_forms'),
    path('login/', admin_one_login_view, name='admin_one_login'),
]