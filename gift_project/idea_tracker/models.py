from django.db import models
from django.forms import ModelForm

class Recipient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField(blank=True)
    notes = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class Gift(models.Model):
    name = models.CharField(max_length=30)
    model_number = models.CharField(max_length=30, blank=True)
    recipients = models.ManyToManyField(Recipient)

    def __str__(self):
        return self.name

class RecipientForm(ModelForm):
    class Meta:
        model = Recipient
        fields = ['first_name', 'last_name', 'birthday', 'notes',
]

class GiftForm(ModelForm):
    class Meta:
        model = Gift
        fields = ['name', 'model_number', 'recipients',
]
