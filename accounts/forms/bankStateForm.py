from django import forms
from ..models import BankState
import datetime

class BankStateForm(forms.ModelForm):
    class Meta:
        model = BankState
        fields = ['BankName', 'BankShortName','LedgerNo','Amount','LatestDate','EditDate']
        # fields = '__all__'  # Use all fields from the model
        # widgets = {
        #     'LatestDate': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        #     'EditDate': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        # }
    
    
    banks_choices = [
        ('Citizen Bank Limited, Surkhet', 'Citizen Bank Limited, Surkhet'),
        ('Nepal Investment Mega Bank Limited', 'Nepal Investment Mega Bank Limited'),
        ('Citizen Bank Limited, HO', 'Citizen Bank Limited, HO'),
        ('Citizen Bank Limited, Narayanghat', 'Citizen Bank Limited, Narayanghat'),
        ('Citizen Bank Limited, Banepa', 'Citizen Bank Limited, Banepa'),
        ('Nabil Bank Limited, HO-5397', 'Nabil Bank Limited, HO-5397'),
        ('Nabil Bank Limited, HO-5399', 'Nabil Bank Limited, HO-5399'),
        ('Citizen Bank Limited, Kohalpur', 'Citizen Bank Limited, Kohalpur'),
        ('Citizen Bank Limited, Tulsipur', 'Citizen Bank Limited, Tulsipur'),
        ('Citizen Bank Limited, Hetauda', 'Citizen Bank Limited, Hetauda'),
        ('Citizen Bank Limited, Jitpur', 'Citizen Bank Limited, Jitpur'),
        ('Citizen Bank Limited, Janakpur', 'Citizen Bank Limited, Janakpur'),
        ('Citizen Bank Limited, HO', 'Citizen Bank Limited, HO'),
        ('Citizen Bank Limited, Taulihawa', 'Citizen Bank Limited, Taulihawa'),
        ('Prime Commercial Bank', 'Prime Commercial Bank'),
        ('Kumari Bank Limited, Kalimati', 'Kumari Bank Limited, Kalimati'),
        ('Garima Bikas Bank Limited, BKT', 'Garima Bikas Bank Limited, BKT'),
        # Add more choices as needed
    ]
    
    # BankName = forms.CharField(
    #     widget = forms.TextInput(attrs={'class': 'form-control'})
    # )
    
    # BankShortName = forms.CharField(
    #     widget = forms.TextInput(attrs={'class': 'form-control'})
    # )
  
    # LedgerNo = forms.CharField(
    #     widget = forms.TextInput(attrs={'class': 'form-control'})
    # )
    
    BankName = forms.ChoiceField(choices=banks_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    BankShortName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    LedgerNo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    
    Amount = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    LatestDate = forms.DateField(
        initial = datetime.date.today,
        widget = forms.DateInput(attrs={'class': 'form-control','type':'date', 'readonly': 'readonly'}),
        required=False  # Depending on whether you want it to be required or not
    )
    EditDate = forms.DateField(
        initial = datetime.date.today,
        widget = forms.DateInput(attrs={'class': 'form-control','type':'date', 'readonly': 'readonly'}),
        required=False  # Depending on whether you want it to be required or not
    )
    