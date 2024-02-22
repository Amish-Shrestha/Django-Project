from django import forms
from ..models import PremiumModel
import datetime

class PremiumForm(forms.ModelForm):
    
    class Meta:
        model = PremiumModel
        fields = ['ProvinceCode','BranchCode','TodayPremium','TotalPremium','EmployeeId','CreatedDate','EditDate']

    
    branch_choices= [
    (702, 'Attariya'),
    (301, 'Bagmati Provience Office'),
    (302, 'Banepa Office'),
    (101, 'Birtamod'),
    (605, 'Chinchu'),
    (600, 'Corporate Office'),
    (703, 'Dadeldhura'),
    (603, 'Dailekh'),
    (402, 'Damauli'),
    (401, 'Gaindakot'),
    (303, 'Hetauda'),
    (102, 'Illam'),
    (604, 'Jajarkot'),
    (202, 'Janakpur'),
    (502, 'Jitpur'),
    (201, 'Kalaiya'),
    (602, 'Kohalpur'),
    (990, 'ONLINE'),
    (1, 'Province 1'),
    (2, 'Province 2'),
    (3, 'Province 3'),
    (4, 'Province 4'),
    (5, 'Province 5'),
    (6, 'Province 6'),
    (7, 'Province 7'),
    (203, 'Rajbiraj'),
    (606, 'Salyan'),
    (304, 'Sindhuli'),
    (601, 'Surkhet'),
    (503, 'Taulihawa'),
    (701, 'Tikapur'),
    (501, 'Tulsipur')
    ] 

    BranchCode = forms.ChoiceField(choices=branch_choices, widget=forms.Select(attrs={'class':'form-control'}))
    ProvinceCode = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))    
    TodayPremium = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    TotalPremium = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    EmployeeId = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': False}))
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