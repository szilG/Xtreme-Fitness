from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Subscribe


class SubscriberForm(forms.ModelForm):
    """Add custom default value to email field """
    email = forms.EmailField(
        label='', widget=forms.EmailInput(
            attrs={'placeholder': 'Your email', 'class': 'form-control'}))

    class Meta:
        """Add model and fields"""
        model = Subscribe
        fields = ('email',)
