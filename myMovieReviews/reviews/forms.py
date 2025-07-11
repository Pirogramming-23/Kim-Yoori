from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        widgets = {
            'genre': forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-group'}),
            'rating': forms.Select(attrs={'class': 'short-select'}),
            'running_time': forms.NumberInput(attrs={'class': 'short-input'}),
        }