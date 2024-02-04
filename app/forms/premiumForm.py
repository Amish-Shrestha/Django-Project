from django import forms
from ..models import PremiumModel
import datetime

class PremiumForm(forms.ModelForm):
    
    class Meta:
        model = PremiumModel
        fields = ['ProvinceCode','BranchCode','TodayPremium','TotalPremium','EmployeeId','CreatedDate','EditDate']

    
    banks_choices= [
        ('a','a')
    ]
    
    ProvinceCode = forms.ChoiceField(choices=banks_choices, widget=forms.Select(attrs={'class':'form-control'}))    
    BranchCode = forms.ChoiceField(choices=banks_choices, widget=forms.Select(attrs={'class':'form-control'}))
    TodayPremium = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    TotalPremium = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    EmployeeId = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    CreatedDate = forms.DateField( 
                                initial = datetime.date.today,
                                widget = forms.DateInput(attrs={'class': 'form-control','type':'date', 'readonly': 'readonly'}),
                                required=True 
    )
    EditDate = forms.DateField( 
                                initial = datetime.date.today,
                                widget = forms.DateInput(attrs={'class': 'form-control','type':'date', 'readonly': 'readonly'}),
                                required=True 
    )