from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'director', 'actors', 'genre', 'rating', 'running_time', 'content']