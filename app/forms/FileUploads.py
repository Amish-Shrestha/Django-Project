from django import forms
from ..models import filesUpload

class MyModelForm(forms.ModelForm):
    class Meta:
        model = filesUpload
        fields = ['file']