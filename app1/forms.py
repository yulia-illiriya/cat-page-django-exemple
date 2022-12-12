from django import forms
from .models import *

class AddCatForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['breed'].empty_label = "Breed isn't chosen"

    class Meta:
        model = Cat
        fields = "__all__" 
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }    
    