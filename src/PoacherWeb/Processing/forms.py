from django import forms
from .models import *

class PoacherForm(forms.ModelForm):
    class Meta:
        model = PoacherImage
        fields = ['ImageName', 'Image']