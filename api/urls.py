from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import *
from django.urls import path, include


router = DefaultRouter()
router.register(r'bankstates', BankStateViewSet, basename='bankstates')

urlpatterns = [
    path('data/', include(router.urls)),
    
    ]