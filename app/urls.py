from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('users/', users, name='users'),
    path('',auth_views.LoginView.as_view(),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#   path('api/token/', obtain_auth_token, name='token_obtain_pair'),
#   path('refresh_session/', views.refresh_session, name='refresh_session'),
]

