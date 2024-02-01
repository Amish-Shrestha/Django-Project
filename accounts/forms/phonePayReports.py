from django import forms
from django.contrib.auth.models import User

class PhonePayReportsForm(forms.Form):
    
    payment_type_method = [
        ('200034', 'Esewa'),
        ('200035', 'PhonePay'),
        # ('wallet', 'Mobile Wallet'),
    ]
    
    payment_type_statues = [
        ('PaymentSuccessful', 'Payement Succesfull'),
        ('Registered', 'Registerd'),
        ('PaymentFailure', 'Payement Failure'),
        # ('wallet', 'Mobile Wallet'),
    ]
    
    
    Payment_statues = forms.ChoiceField(
        choices=payment_type_statues,
        widget=forms.Select(attrs={'class': 'form-control'}),  # Add optional styling class
    )
    
    Payment_type = forms.ChoiceField(
        choices=payment_type_method,
        widget=forms.Select(attrs={'class': 'form-control'}),  # Add optional styling class
    )
        
        
    StartDate = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'datepicker',  # Add a CSS class for styling
                'placeholder': 'Select a date',  # Add a placeholder text
                'type': 'date'
            }
        )
    )
    EndDate = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'datepicker',  # Add a CSS class for styling
                'placeholder': 'Select a date',  # Add a placeholder text
                'type': 'date'
            }
        )
    )
