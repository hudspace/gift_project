from django.forms import ModelForm
from datetime import date
from django import forms
from . import models

class RecipientForm(ModelForm):
    class Meta:
        model = models.Recipient
        widgets = {
            'birthday': forms.TextInput(attrs={'placeholder': 'ex: 11/17/2017'}),
        }
        fields = ['first_name', 'last_name', 'birthday', 'notes',]


class GiftForm(ModelForm):
    class Meta:
        model = models.Gift
        help_texts = {
            'recipients': 'Click on an intended recipient',
        }
        fields = ['name', 'model_number', 'price', 'recipients', 'purchased']


