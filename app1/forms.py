from django import forms
from .models import *
from django.core.exceptions import ValidationError

class AddCatForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['breed'].empty_label = "Breed isn't chosen"

    class Meta:
        model = Cat
        fields = "__all__" 
           

    def clean_title(self):
        name = self.cleaned_data['name']
        if len(name) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return name
    