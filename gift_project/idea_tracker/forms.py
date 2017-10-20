from django.forms import ModelForm

from datetime import date

from django import forms

from . import models

class RecipientForm(ModelForm):
    class Meta:
        model = models.Recipient
        fields = ['first_name', 'last_name', 'birthday', 'notes',]

class GiftForm(ModelForm):
    class Meta:
        model = models.Gift
        fields = ['name', 'model_number', 'price', 'recipients', 'purchased']
