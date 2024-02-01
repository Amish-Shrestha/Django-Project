from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('account/bankstate', bankStateClass.view_bankstate, name='bankstate'),
    path('bankstate/add', bankStateClass.create_bankstate, name='create_bankstate'),
    path('bankstate/edit', bankStateClass.edit_bankstate, name='edit_bankstate'),
    path('bankstate/delete/<int:pk>/', bankStateClass.delete_bankstate, name='delete_bankstate'),
    path('account/phonepayreports', PhonePayReportView.phonepay, name='phonepay'),
    path('account/BankBalance', BankBalanceView.BankBalanceStatements, name='BankBalanceStatements'),
]

