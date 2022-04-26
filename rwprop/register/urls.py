from django.urls import path, re_path

from . import views
from django.contrib.auth import views as auth


urlpatterns = [
    path('acc/login/', views.login_, name='login'),
    path('acc/logout/', auth.LogoutView.as_view(), name='logout'),
    path('acc/register/', views.register, name='register'),
]
