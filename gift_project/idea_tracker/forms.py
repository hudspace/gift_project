from django.forms import ModelForm

from datetime import date

from django import forms

from . import models

class RecipientForm(ModelForm):
    class Meta:
        model = models.Recipient
        fields = ['first_name', 'last_name', 'birthday', 'notes',]

    def clean_birthday(request, self):
        if request.method == 'POST':
            if self.birthday >= datetime.date:
                print('Please enter a valid birthday')
            else:
                birthday = self.birthday
        return birthday



class GiftForm(ModelForm):
    class Meta:
        model = models.Gift
        fields = ['name', 'model_number', 'recipients',]
