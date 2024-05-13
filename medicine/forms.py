from django import forms
from .models import Medicine


class MedisineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['title', 'description', 'image']
