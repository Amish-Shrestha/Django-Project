from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('users/', users, name='users'),
    path('premium/', PremiumData.PremimumView, name='premium' ),
    path('premium/add', PremiumData.CrestPremium, name='creat_premium' ),
    path('premium/edit', PremiumData.EditPremium, name='edit_premium' ),
    path('premium/delete/<int:pk>/', PremiumData.DeletePremium, name='delete_premium' ),
    path('',auth_views.LoginView.as_view(),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#   path('api/token/', obtain_auth_token, name='token_obtain_pair'),
#   path('refresh_session/', views.refresh_session, name='refresh_session'),
]

