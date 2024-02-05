from django import forms

class BatchIdForm(forms.Form):
    BatchId = forms.CharField (
        widget = forms.TextInput(
        attrs = {
            'type' :'text'
        },
    )
)